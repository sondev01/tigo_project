import json

from odoo import http
from odoo.http import request
from odoo.tools import date_utils


class ApplicableController(http.Controller):

    @http.route('/api/applicable_type', auth='public', methods=['GET'], type='http', csrf=False)
    def get_applicable(self):
        tasks = http.request.env['applicable.type'].sudo().search([])
        data = tasks.read(['name'])
        json_data = json.dumps(data, default=date_utils.json_default)
        return json_data

    @http.route('/api/applicable_type', auth='public', methods=['POST'], type='http', csrf=False)
    def delete_product(self, **kwargs):
        products = request.env['applicable.type'].sudo().create(kwargs)
        product = products.read(['code', 'name'])
        return json.dumps(product)

    @http.route('/api/school_models', auth='public', methods=['GET'], type='http', csrf=False)
    def get_school(self):
        data_schools = request.env['school.models'].sudo().search([])
        data_school = data_schools.read()
        return json.dumps(data_school, default=date_utils.json_default)

    @http.route('/api/school_models', auth='public', methods=['POST'], type='http', csrf=False)
    def post_school(self, **kwargs):
        data_schools = request.env['school.models'].sudo().create(kwargs)
        data_school = data_schools.read(['name', 'code'])
        return json.dumps(data_school)

    @http.route('/api/school_models', auth='public', methods=['PUT'], type='http', csrf=False)
    def put_school(self, id, **kwargs):
        data_schools = request.env['school.models'].sudo().search([('id', '=', id)])
        data_schools.write(kwargs)
        return json.dumps({'message': 'Done'})

    @http.route('/api/school_models', auth='public', methods=['DELETE'], type='http', csrf=False)
    def delete_school(self, id):
        data_schools = request.env['school.models'].sudo().browse(id)
        data_schools.unlink()
        return json.dumps({'message': 'Done'})
