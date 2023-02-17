# -*- coding: utf-8 -*-

from odoo import models, api, fields


class AppliedSubjects(models.Model):
    _name = 'applied.subjects'
    _description = 'Môn học áp dụng'

    name_subjects = fields.Char(string="Tên môn học", required=True)
    code = fields.Char(string="Mã môn học", required=True)
