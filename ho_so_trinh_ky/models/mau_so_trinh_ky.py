# -*- coding: utf-8 -*-

from odoo import models, api, fields


class MauSoTrinhKy(models.Model):
    _name = 'mauso.trinhky'
    _description = 'Mẫu sổ trình ký'

    name = fields.Char(string="Tên sổ", required=True)
    sl_chua_ky = fields.Integer(string="Số lượng chưa trình ký", readonly=True, default=0)
    sl_dang_ky = fields.Integer(string="Số lượng đang trình ký", readonly=True, default=0)
    sl_duyet_so = fields.Integer(string="Số lượng duyệt kí sổ", readonly=True, default=0)
    sl_tu_choi = fields.Integer(string="Số lượng từ chối", readonly=True, default=0)

    def see_more(self):
        self.ensure_one()
        return self._get_action('ho_so_trinh_ky.hoso_trinhky_view')

    def _get_action(self, action_xmlid):
        action = self.env["ir.actions.actions"]._for_xml_id(action_xmlid)
        domain = [('mau_so_trinhky_id.name', '=', self.name)]
        action['domain'] = domain
        return action

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


