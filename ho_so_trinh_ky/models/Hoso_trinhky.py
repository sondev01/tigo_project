# -*- coding: utf-8 -*-

from odoo import models, api, fields


class HoSoTrinhKy(models.Model):
    _name = 'hoso.trinhky'
    _description = 'Hồ sơ trình ký'
    _rec_name = 'ten_hoso'

    ten_hoso = fields.Char(string="Tên Hồ Sơ", required=True)
    trang_thai_so = fields.Selection([
        ('draft', 'Chưa trình ký'),
        ('doing', 'Đang ký Sổ'),
        ('use', 'Duyệt ký Sổ'),
        ('cancel', 'Từ chối ký Sổ')], string='Trạng thái', default='draft')
    file = fields.Binary(string='File Nộp', required=True)
    khoihoc_apdung_id = fields.Many2one('applied.learning', string='Khối học')
    monhoc_apdung_id = fields.Many2one('applied.subjects', string='Môn học')
    ngay_nop = fields.Date(string='Ngày nộp', required=True)
    nguoi_nop = fields.Many2many('res.users', 'ho_so_res_user_ref', 'ho_so_id', 'res_user_id', string='Người nộp',
                                 required=True)
    nhan_xet = fields.Char(string='Nhận xét')
    da_ky_dien_tu = fields.Boolean(string=' Đã ký điện tử')
    mau_so_trinhky_id = fields.Many2one('list.sample', string="Mẫu sổ trình ký", requred=True)

    @api.onchange('mau_so_trinhky_id')
    def onchange_mau_so_trinh_ki(self):
        for r in self:
            r.nguoi_nop = r.mau_so_trinhky_id.object_ids.ids

    def use(self):
        for r in self:
            r.trang_thai_so = 'use'
            r.update_record()

    def doing(self):
        for r in self:
            r.trang_thai_so = 'doing'
            r.update_record()

    def draft(self):
        for r in self:
            r.trang_thai_so = 'draft'
            r.update_record()

    def cancel(self):
        for r in self:
            r.trang_thai_so = 'cancel'
            r.update_record()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Nhận Xét',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'popup.cmt',
            'views': [(self.env.ref('ho_so_trinh_ky.popup_cmt_view').id, 'form')],
            'target': 'new',
        }

    @api.model
    def create(self, vals_list):
        name_record = self.env['list.sample'].search([('id', '=', vals_list['mau_so_trinhky_id'])]).name
        mau_so = self.env['mauso.trinhky'].search([('name', '=', name_record)])
        if not mau_so:
            self._cr.execute(f'''
                           INSERT INTO mauso_trinhky (name,sl_chua_ky,sl_dang_ky,sl_duyet_so,sl_tu_choi)
                           VALUES  ('{name_record}',1,0,0,0)
                           ''')
        else:
            self._cr.execute(f'''
                                update mauso_trinhky mt 
                                set sl_chua_ky = {mau_so.sl_chua_ky + 1} 
                                where mt.name = '{name_record}' ''')
        return super(HoSoTrinhKy, self).create(vals_list)

    def unlink(self):
        for r in self:
            record_number = self.env['mauso.trinhky'].search([('name', '=', r.mau_so_trinhky_id.name)])
            self_record = self.search([('ten_hoso', '=', r.ten_hoso)])
            if len(self_record) == 1:
                self.env['mauso.trinhky'].search([('name', '=', r.mau_so_trinhky_id.name)]).unlink()
            else:
                if self.trang_thai_so == 'draft':
                    self.update_record_unlink(record_number.sl_chua_ky, r.mau_so_trinhky_id.name)
                elif self.trang_thai_so == 'doing':
                    self.update_record_unlink(record_number.sl_dang_ky, r.mau_so_trinhky_id.name)
                elif self.trang_thai_so == 'use':
                    self.update_record_unlink(record_number.sl_duyet_so, r.mau_so_trinhky_id.name)
                else:
                    self.update_record_unlink(record_number.sl_tu_choi, r.mau_so_trinhky_id.name)

        return super(HoSoTrinhKy, self).unlink()

    def update_record_unlink(self, sl, name):
        self._cr.execute(f'''
                            update mauso_trinhky mt 
                            set sl_chua_ky = {sl - 1} 
                            where mt.name = '{name}' ''')

    def update_record(self):
        self._cr.execute(f'''
                            update mauso_trinhky mt
                            set 
                            sl_chua_ky = tb.draft,
                            sl_dang_ky = tb.doing,
                            sl_duyet_so = tb.use,
                            sl_tu_choi = tb.cancel
                            from (
                                SELECT sum(case when st.trang_thai_so = 'draft'  then 1 else 0 end) as draft,
                                     sum(case when st.trang_thai_so = 'doing'  then 1 else 0 end) as doing,
                                     sum(case when st.trang_thai_so = 'use'  then 1 else 0 end) as use,
                                     sum(case when st.trang_thai_so = 'cancel'  then 1 else 0 end) as cancel,
                                     ls.name as name
                                from hoso_trinhky st 
                                LEFT JOIN list_sample ls ON st.mau_so_trinhky_id = ls.id
                                WHERE st.mau_so_trinhky_id = {self.mau_so_trinhky_id.id}
                                group by ls.name ) AS tb (draft,doing,use,cancel, name)
    
                            where mt.name = tb.name
                            ''')
