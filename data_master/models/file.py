from odoo import models, api, fields


class FileModels(models.Model):
    _name = 'file.models'
    _description = 'Định dạng tệp'

    name = fields.Char('Tên định dạng')
