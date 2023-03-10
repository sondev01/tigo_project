# -*- coding: utf-8 -*-

from odoo import models, api, fields


class ApplicableType(models.Model):
    _name = 'applicable.type'
    _description = 'Loại áp dụng'

    name = fields.Char(string='Loại áp dụng', required=True)
    code = fields.Char(string='Mã loại áp dụng', required=True)
