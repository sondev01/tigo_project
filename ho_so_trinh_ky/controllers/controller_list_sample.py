import json
from odoo import http
from odoo.http import request


class ControllerListSample(http.Controller):

    @http.route('/api/list_sample', auth='public', methods=['GET'], type='http', csrf=False)
    def get_data(self):
        get_datas = request.env['list.sample'].sudo().search([])
        get_data = get_datas.read(['name', 'state', 'applicable_type_id', 'tan_so', 'frequency_id'])
        return json.dumps(get_data)

    @http.route('/api/list_sample', auth='public', methods=['POST'], type='http', csrf=False)
    def post_data(self, **kwargs):
        request.env['list.sample'].sudo().create(kwargs)
        return json.dumps({'Message': 'Done'})

    @http.route('/api/list_sample', auth='public', methods=['PUT'], type='http', csrf=False)
    def put_data(self, id, **kwargs):
        record_datas = request.env['list.sample'].sudo().browse(id)
        record_datas.write(kwargs)
        return json.dumps({'Message': 'Done'})

    @http.route('/api/list_sample', auth='public', methods=['DELETE'], type='http', csrf=False)
    def delete_data(self, id):
        record_datas = request.env['list.sample'].sudo().browse(id)
        record_datas.unlink()
        return json.dumps({'Message': 'Done'})
