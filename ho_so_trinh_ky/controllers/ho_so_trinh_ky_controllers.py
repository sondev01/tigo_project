import json
from odoo import http
from odoo.http import request


class ControllerHoSo(http.Controller):

    @http.route('/api/ho_so_trinh_ky', auth='none', methods=['GET'], type='http', csrf=False)
    def get_data(self):
        datas_hoso = request.env['hoso.trinhky'].sudo().search([])
        data_hoso = datas_hoso.read(['ten_hoso', 'trang_thai_so', 'khoihoc_apdung_id', 'monhoc_apdung_id'])
        return json.dumps(data_hoso)

    @http.route('/api/ho_so_trinh_ky', auth='none', methods=['POST'], type='http', csrf=False)
    def post_data(self, **kwargs):
        post_datas = request.env['hoso.trinhky'].sudo().create(kwargs)
        post_data = post_datas.read(['ten_hoso', 'trang_thai_so', 'khoihoc_apdung_id', 'monhoc_apdung_id'])
        return json.dumps(post_data)

    @http.route('/api/ho_so_trinh_ky', auth='none', methods=['PUT'], type='http', csrf=False)
    def put_data(self, id, **kwargs):
        record_data = request.env['hoso.trinhky'].sudo().browse(id)
        record_data.write(kwargs)
        return json.dumps({'message': 'Done'})

    @http.route('/api/ho_so_trinh_ky', auth='none', methods=['DELETE'], type='http', csrf=False)
    def delete_data(self, id):
        record_data = request.env['hoso.trinhky'].sudo().browse(id)
        record_data.unlink()
        return json.dumps({'message': 'Done'})
