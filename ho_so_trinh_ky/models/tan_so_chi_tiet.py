from odoo import fields, models, api


class TanSoChiTiet(models.Model):
    _name = 'tanso.chitiet'
    _description = 'Tần số chi tiết'

    name = fields.Integer(string='Số lần', required=True)
    don_vi = fields.Many2one('frequency.models', string='Đơn vị', required=True)
