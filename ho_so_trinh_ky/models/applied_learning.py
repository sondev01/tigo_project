# -*- coding: utf-8 -*-

from odoo import models, api, fields


class AppliedLearning(models.Model):
    _name = 'applied.learning'
    _description = 'Khối học áp dụng'
    _rec_name = 'name_blocks'

    name_blocks = fields.Char(string="Tên khối học", required=True)
    code = fields.Char(string="Mã khối học", required=True)
