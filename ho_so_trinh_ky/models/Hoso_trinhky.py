# -*- coding: utf-8 -*-

from odoo import models, api, fields


class HoSoTrinhKy(models.Model):
    _name = 'hoso.trinhky'
    _description = 'Hồ sơ trình ký'

    ten_hoso = fields.Char(string="Tên Hồ Sơ", required=True)
    # ky_nop_id = fields.Many2one('',string='Kỳ nộp')
    trang_thai_so = fields.Selection([
        ('draft', 'Nháp'),
        ('use', 'Sử dụng'),
        ('block', 'Khóa'),
        ('all', 'Tất cả'),
        ('cancel', 'Từ chối')], string='Trạng thái', default='draft')
    file = fields.Binary(string='File Nộp', required=True)
    khoihoc_apdung = fields.Many2one('applied.learning', string='Khối học', reuired=True)
    monhoc_apdung = fields.Many2one('applied.subjects', string='Môn học', required=True)
    ngay_nop = fields.Date(string='Ngày nộp', required=True)
    nguoi_nop = fields.Char(string='Người nộp', required=True)
    duong_dan = fields.Char(string='Đường dẫn')
    nhan_xet = fields.Char(string='Nhận xét')
    mau_so = fields.Many2one('list.sample', string="Mẫu sổ", required=True)
    da_ky = fields.Boolean(string='đã ký')
    da_ky_dien_tu = fields.Boolean(string=' Đã ký điện tử')
