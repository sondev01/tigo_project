from odoo import api, fields, models


class SoKyDuyet(models.Model):
    _name = 'so.ky'
    _description = 'Danh mục sổ ký duyệt'

    sl_cho_ky = fields.Integer('Số lượng hồ sơ chờ ký')
    name = fields.Char('Tên sổ')
    state_so = fields.Selection([
        ('not_use', 'Chưa sử dụng'),
        ('use', 'Sử dụng')], string="Trạng thái sổ")
    loai_ap_dung_id = fields.Many2one('res.groups', string='Loại áp dụng')
    tuan_suat = fields.Char(string='Tần suất')
    state_ky = fields.Selection([
        ('pending', 'Chờ kí'),
        ('done', 'Đã ký')], string='Trạng thái ký sổ')

    def ky_duyet(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Hồ sơ trình ký',
            'view_mode': 'tree,form',
            'res_model': 'hoso.trinhky',
            'domain': [('trang_thai_so', '=', 'draft'), ('mau_so_trinhky_id.name', '=', self.name)],
            'target': 'current',
        }
