# -*- coding: utf-8 -*-

from odoo import models, api, fields


class Education(models.Model):
    _name = 'education.models'
    _description = 'Phòng giáo dục'

    name = fields.Char('Tên phòng giáo dục')
    education_code = fields.Char('Mã phòng giáo dục')