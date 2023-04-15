from odoo import models, api, fields


class SignBook(models.Model):
    _name = "sign.book"
    _description = 'Đối tượng kí duyệt sổ'

    order_of_signing = fields.Integer(string='Thứ tự kí')
    model_name_id = fields.Many2one("list.sample", string='Tên mẫu sổ')
    object_type_id = fields.Many2one('res.groups', string='Loại đối tượng kí')
    signature = fields.Boolean(string='Thực hiện ký điện tử')
    promulgate = fields.Boolean(string='Ban hành')
    list_sample_id = fields.Many2one('list.sample', string='Danh mục mẩu sổ')
