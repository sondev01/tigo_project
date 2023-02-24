# -*- coding: utf-8 -*-

from odoo import models, api, fields


class MauSoTrinhKy(models.Model):
    _name = 'mauso.trinhky'
    _description = 'Mẫu sổ trình ký'

    name = fields.Many2one('list.smaple',string="Tên sổ", required=True)
    state = fields.Selection([
        ('draft', 'Nháp'),
        ('use', 'Sử dụng'),
        ('block', 'Khóa'),
        ('all', 'Tất cả'),
        ('cancel', 'Từ chối')], string='Trạng thái', default='draft')
    sl_chua_ky = fields.Integer(string="Số lượng chưa trình ký", readonly=True, default=0, compute="_compute_state")
    sl_dang_ky = fields.Integer(string="Số lượng đang trình ký", readonly=True, default=0, compute="_compute_state")
    sl_duyet_so = fields.Integer(string="Số lượng duyệt kí sổ", readonly=True, default=0, compute="_compute_state")
    sl_tu_choi = fields.Integer(string="Số lượng từ chối", readonly=True, default=0, compute="_compute_state")
    loai_ap_dung_id = fields.Many2one("applicable.type", string="Loại áp dụng", required=True)
    tan_suat_id = fields.Many2one('frequency.models', string='Tần suất', required=True)
    cap_hoc_id = fields.Many2one('school.level', string="Cấp học")

    def see_more(self):
        self.ensure_one()
        return self._get_action('ho_so_trinh_ky.hoso_trinhky_view')

    def _get_action(self, action_xmlid):
        action = self.env["ir.actions.actions"]._for_xml_id(action_xmlid)
        domain = [('mau_so_trinhky_id', '=', self.id)]
        action['domain'] = domain
        return action

    def _compute_state(self):
        for r in self:
            r.sl_chua_ky = self.env['hoso.trinhky'].search_count(
                [('trang_thai_so', '=', 'draft'), ('mau_so_trinhky_id', '=', r.id)])
            r.sl_dang_ky = self.env['hoso.trinhky'].search_count(
                [('trang_thai_so', '=', 'use'), ('mau_so_trinhky_id', '=', r.id)])
            r.sl_duyet_so = self.env['hoso.trinhky'].search_count(
                [('trang_thai_so', '=', 'block'), ('mau_so_trinhky_id', '=', r.id)])
            r.sl_tu_choi = self.env['hoso.trinhky'].search_count(
                [('trang_thai_so', '=', 'cancel'), ('mau_so_trinhky_id', '=', r.id)])

    def use(self):
        for r in self:
            r.state = 'use'

    def block(self):
        for r in self:
            r.state = 'block'

    def all(self):
        for r in self:
            r.state = 'all'

    def cancel(self):
        for r in self:
            r.state = 'cancel'
