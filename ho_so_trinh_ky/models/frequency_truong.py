# -*- coding: utf-8 -*-

from odoo import models, api, fields


class FrequencyModels(models.Model):
    _name = 'frequency.models'
    _description = 'Tần suất'

    name = fields.Char('Đơn vị', required=True)
