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

    # @api.onchange('mau_so_trinhky_id')
    # def onchange_mau_so_trinh_ki(self):
    #     for r in self:
    #         r.nguoi_nop = r.mau_so_trinhky_id.groups_ids.ids

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

        return {
            'type': 'ir.actions.act_window',
            'name': 'Nhận Xét',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'popup.cmt',
            'views': [(self.env.ref('ho_so_trinh_ky.popup_cmt_view').id, 'form')],
            'target': 'new',
        }

    @api.onchange('mau_so_trinhky_id')
    def _onchange_nguoi_nop(self):
        for r in self:
            sql = '''
                SELECT distinct (uid) FROM res_groups_users_rel WHERE gid in {}
            '''.format(tuple(r.mau_so_trinhky_id.groups_ids.ids + [0, 0]))
            self._cr.execute(sql)
            recs = self._cr.dictfetchall()
            list_id = []
            for rec in recs:
                list_id.append(rec['uid'])
        return {'domain': {'nguoi_nop': [('id', 'in', list_id)]}}
