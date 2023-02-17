from odoo import models, api, fields


class School(models.Model):
    _name = 'school.models'
    _description = 'Trường học'

    name = fields.Char('Tên trường', required=True)
    code = fields.Char('Mã trường', required=True)
