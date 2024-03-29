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
    name = fields.Char(string="Danh mục mẫu sổ")
    applicable_type_id = fields.Many2one('applicable.type', string='Loại áp dụng')
    tan_so = fields.Integer(string='Tần suất')
    frequency_id = fields.Many2one('frequency.models', string="Tần suất")
    from_date = fields.Date(string='Từ ngày')
    to_date = fields.Date(string='Đến ngày')
    choose_signer = fields.Boolean(string="Cho chọn người ký duyệt áp dụng")
    outsider_signer = fields.Boolean(string="Cho phép đơn vị ngoài nộp")
    check_done = fields.Boolean(string='Xác nhận hoàn thành')
    applied_learning_ids = fields.Many2many('applied.learning',
                                            'list_sample_applied_learning_ref',
                                            'list_sample_id',
                                            'applied_learning_id', string="Khối học áp dụng")
    applied_subjects_ids = fields.Many2many('applied.subjects',
                                            'list_sample_applied_subjects_ref',
                                            'list_sample_id',
                                            'applied_subjects', string='Môn học áp dụng')
    school_level_ids = fields.Many2many('school.level',
                                        'list_sample_school_level_ref',
                                        'list_sample_id',
                                        'school_level_id', string="Cấp học")
    education_ids = fields.Many2many('education.models',
                                     'list_sample_education_models_ref',
                                     'list_sample_id',
                                     'education_id', string="Phòng giáo dục")
    school_ids = fields.Many2many('school.models',
                                  'list_sample_school_ref',
                                  'list_sample_id',
                                  'school_id', string="Trường")
    file_ids = fields.Many2many('file.models',
                                'list_sample_file_ref',
                                'list_sample_id',
                                'file_id', string="File")
    groups_ids = fields.Many2many('res.groups',
                                  'list_sample_object_ref',
                                  'list_sample_id',
                                  'groups_id', string="Nhóm đối tượng nộp")
    sign_book_ids = fields.One2many('sign.book', 'list_sample_id', string='đối tượng kí duyệt sổ')
    check = fields.Boolean('Kiểm tra dữ liệu', invisible=True, defautl=False)
    check1 = fields.Boolean('Kiểm tra dữ liệu', invisible=True)  # loại áp dụng khi chọn sở và trường ko hiện ts2
    check2 = fields.Boolean('Kiểm tra dữ liệu', invisible=True)  # invisible để ẩn nút check

    @api.onchange('frequency_id')
    def _onchange_frequency_id(self):
        for r in self:
            if r.frequency_id.name == 'Tự định nghĩa':
                r.check = True
            else:
                r.check = False

    @api.onchange('applicable_type_id')
    def _onchange_applicable_type_id(self):
        for r in self:
            if r.applicable_type_id.name in ('nội bộ sở', 'trường'):
                r.check1 = True
            else:
                r.check1 = False
            if r.applicable_type_id.name == "GVBM":  # khi chọn loại áp dụng GVMB thì hiện thêm chọn khối Khối
                r.check2 = True
            else:
                r.check2 = False

    @api.model
    def create(self, vals_list):
        res = super(ListSamples, self).create(vals_list)
        result = self.env['mauso.trinhky'].search_count([('name', '=', vals_list['name'])])
        if result == 0:
            self.env['mauso.trinhky'].create({'name': vals_list['name']})
        return res