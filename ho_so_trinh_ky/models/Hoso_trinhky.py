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
    nguoi_nop = fields.Char(string='Người nộp', required=True)
    nhan_xet = fields.Char(string='Nhận xét')
    da_ky_dien_tu = fields.Boolean(string=' Đã ký điện tử')
    mau_so_trinhky_id = fields.Many2one('list.sample', string="Mẫu sổ trình ký", requred=True)

    def use(self):
        for r in self:
            r.trang_thai_so = 'use'

    def doing(self):
        for r in self:
            r.trang_thai_so = 'doing'

    def draft(self):
        for r in self:
            r.trang_thai_so = 'draft'

    def cancel(self):
        for r in self:
            r.trang_thai_so = 'cancel'

    @api.constrains('mau_so_trinhky_id', 'trang_thai_so')
    def constrains_ten_ho_so(self):
        for r in self:
            name_models = self.env['mauso.trinhky'].search([('name', '=', r.mau_so_trinhky_id.name)])
            if len(name_models) == 0:
                if r.trang_thai_so == 'draft':
                    self._cr.execute(f'''
                                    INSERT INTO mauso_trinhky (name,sl_chua_ky,sl_dang_ky,sl_duyet_so,sl_tu_choi)
                                    VALUES  ('{r.mau_so_trinhky_id.name}',1,0,0,0)
                                    ''')
            else:
                print(self._cr.execute(f'''
                                update mauso_trinhky 
                                set 
                                sl_chua_ky = tb.draft,
                                sl_dang_ky = tb.doing,
                                sl_duyet_so = tb.use,
                                sl_tu_choi = tb.cancel
                                from (
                                    SELECT sum(case when st.trang_thai_so = 'draft'  then 1 else 0 end) as draft,
                                         sum(case when st.trang_thai_so = 'doing'  then 1 else 0 end) as doing,
                                         sum(case when st.trang_thai_so = 'use'  then 1 else 0 end) as use,
                                         sum(case when st.trang_thai_so = 'cancel'  then 1 else 0 end) as cancel
                                    from hoso_trinhky st 
                                    WHERE st.mau_so_trinhky_id = {self.mau_so_trinhky_id.id}) AS tb (draft,doing,use,cancel)
                                '''))
