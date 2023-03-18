# -*- coding: utf-8 -*-

from odoo import models, api, fields


class MauSoTrinhKy(models.Model):
    _name = 'mauso.trinhky'
    _description = 'Mẫu sổ trình ký'

    name = fields.Char(string="Tên sổ", required=True)
    sl_chua_ky = fields.Integer(string="Số lượng chưa trình ký", readonly=True, default=0, compute='_compute_data')
    sl_dang_ky = fields.Integer(string="Số lượng đang trình ký", readonly=True, default=0, compute='_compute_data')
    sl_duyet_so = fields.Integer(string="Số lượng duyệt kí sổ", readonly=True, default=0, compute='_compute_data')
    sl_tu_choi = fields.Integer(string="Số lượng từ chối", readonly=True, default=0, compute='_compute_data')

    def see_more(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Hồ sơ trình kí',
            'res_model': 'hoso.trinhky',
            'view_mode': 'tree,form',
            'target': 'current',
        }

    def _compute_data(self):
        for r in self:
            r.sl_chua_ky = self.env['hoso.trinhky'].search_count(
                [('trang_thai_so', '=', 'draft'), ('mau_so_trinhky_id.name', '=', r.name)])
            r.sl_dang_ky = self.env['hoso.trinhky'].search_count(
                [('trang_thai_so', '=', 'doing'), ('mau_so_trinhky_id.name', '=', r.name)])
            r.sl_duyet_so = self.env['hoso.trinhky'].search_count(
                [('trang_thai_so', '=', 'use'), ('mau_so_trinhky_id.name', '=', r.name)])
            r.sl_tu_choi = self.env['hoso.trinhky'].search_count(
                [('trang_thai_so', '=', 'cancel'), ('mau_so_trinhky_id.name', '=', r.name)])
