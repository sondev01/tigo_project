# -*- coding: utf-8 -*-

from odoo import models, api, fields


class FrequencyModels(models.Model):
    _name = 'frequency.models'
    _description = 'Tần suất'

    name = fields.Char('Đơn vị', required=True)
    numbers = fields.Integer('Số lần', required=True)