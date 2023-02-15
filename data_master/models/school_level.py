# -*- coding: utf-8 -*-

from odoo import models, api, fields


class SchoolLevel(models.Model):
    _name = 'school.level'
    _description = 'Cấp học'

    name = fields.Char('Tên cấp học')
    school_level_code = fields.Char('Mã cấp học')