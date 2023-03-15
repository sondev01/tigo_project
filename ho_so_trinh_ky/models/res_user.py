# -*- coding: utf-8 -*-
from odoo import fields, models


class CustomizeUser(models.Model):
    _inherit = 'res.users'

    x_school_models_id = fields.Many2one('school.models', string='Trường')
