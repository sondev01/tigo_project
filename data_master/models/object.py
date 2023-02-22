from odoo import models, api, fields


class ObjectModels(models.Model):
    _name = 'object.models'
    _description = 'Đối tượng'

    name = fields.Char('Tên đối tượng', required=True)
    code = fields.Char('Mã đối tượng', required=True)
