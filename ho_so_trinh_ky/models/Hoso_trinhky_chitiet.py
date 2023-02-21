# -*- coding: utf-8 -*-

from odoo import models, api, fields


class HoSoTrinhKyChiTiet(models.Model):
    _name = 'trinhky.chitiet'
    _description = 'Hồ sơ trình ký chi tiết'
    _rec_name = 'ho_ten'

    ho_ten = fields.Char(string="Họ và tên", required=True)
    thu_tu_ky = fields.Integer(string="Thứ tự ký", required=True)
    loai_doi_tuong_ky_ids = fields.Many2one('object.models', string="Loại đối tượng ký", required=True)
    ky_dien_tu = fields.Boolean(string='Thực hiện ký điện tử')
    ban_hanh = fields.Boolean(string='Ban hành')
    ten_mau_so_id = fields.Many2one('list.sample', string='Tên mẫu sổ',required=True)
    trang_thai_so = fields.Selection([
        ('draft', 'Nháp'),
        ('use', 'Sử dụng'),
        ('block', 'Khóa'),
        ('all', 'Tất cả'),
        ('cancel', 'Từ chối')], string='Trạng thái', default='draft')
    ho_so_trinh_ky_id = fields.Many2one('hoso.trinhky',string='Hồ sơ trình ký',required=True)

