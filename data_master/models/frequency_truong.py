# -*- coding: utf-8 -*-

from odoo import models, api, fields


class FrequencyModels(models.Model):
    _name = 'frequency.models'
    _description = 'Tần suất'

    name = fields.Char('Đơn vị', required=True)
    numbers = fields.Integer('Số lần', required=True)

    def name_get(self):
        res = []
        for record in self:
            if record.numbers == 0:
                res.append((record.id, record.name))
            else:
                res.append((record.id, "%s/%s" % (record.numbers, record.name)))
        return res
