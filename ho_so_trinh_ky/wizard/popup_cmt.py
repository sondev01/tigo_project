from odoo import models, fields


class PopupCmt(models.TransientModel):
    _name = 'popup.cmt'

    nhan_xet = fields.Char(string='Nhận xét')

    def popup_cmt(self):
        ho_so_trinh_ki_id = self.env.context.get('active_id', False)
        record_values = self.env['hoso.trinhky'].browse(ho_so_trinh_ki_id)
        record_values.nhan_xet = self.nhan_xet
