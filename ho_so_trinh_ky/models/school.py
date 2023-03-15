from odoo import models, api, fields


class School(models.Model):
    _name = 'school.models'
    _description = 'Trường học'

    name = fields.Char('Tên trường', required=True)
    code = fields.Char('Mã trường', required=True)
    level_id = fields.Many2one('school.level', string='Cấp học', required=True)
    edu_dp_id = fields.Many2one('education.models', string='Phòng giáo dục', required=True)
