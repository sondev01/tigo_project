# -*- coding: utf-8 -*-

from odoo import models, api, fields


class ListSamples(models.Model):
    _name = 'list.sample'
    _description = 'Danh mục mẫu sổ'

    state = fields.Selection([
        ('draft', 'Nháp'),
        ('use', 'Sử dụng'),
        ('block', 'Khóa'),
        ('all', 'Tất cả'),
        ('cancel', 'Từ chối')], string='Trạng thái', default='draft')
    name = fields.Char(string="Danh mục mẫu sổ", required=True)
    applicable_type_id = fields.Many2one('applicable.type', string='Loại áp dụng', required=True)
    frequency_id = fields.Many2one('frequency.models', string="Tần suất")
    from_date = fields.Date(string='Từ ngày')
    to_date = fields.Date(string='Đến ngày')
    choose_signer = fields.Boolean(string="Cho chọn người ký duyệt áp dụng")
    outsider_signer = fields.Boolean(string="Cho phép đơn vị ngoài nộp")
    check_done = fields.Boolean(string='Xác nhận hoàn thành')
    applied_learning_ids = fields.Many2many('applied.learning',
                                            'list_sample_applied_learning_ref',
                                            'list_sample_id',
                                            'applied_learning_id', string="Khối học áp dụng", required=True)
    applied_subjects_ids = fields.Many2many('applied.subjects',
                                            'list_sample_applied_subjects_ref',
                                            'list_sample_id',
                                            'applied_subjects', string='Môn học áp dụng', required=True)
    school_level_ids = fields.Many2many('school.level',
                                        'list_sample_school_level_ref',
                                        'list_sample_id',
                                        'school_level_id', string="Cấp học", required=True)
    education_ids = fields.Many2many('education.models',
                                     'list_sample_education_models_ref',
                                     'list_sample_id',
                                     'education_id', string="Phòng giáo dục", required=True)
    school_ids = fields.Many2many('school.models',
                                  'list_sample_school_ref',
                                  'list_sample_id',
                                  'school_id', string="Trường", required=True)
    file_ids = fields.Many2many('file.models',
                                'list_sample_file_ref',
                                'list_sample_id',
                                'file_id', string="File", required=True)
    object_ids = fields.Many2many('object.models',
                                  'list_sample_object_ref',
                                  'list_sample_id',
                                  'object_id', string="Đối tượng nộp", required=True)
    sign_book_ids = fields.One2many('sign.book', 'list_sample_id', string='đối tượng kí duyệt sổ')
