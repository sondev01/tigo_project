# -*- coding: utf-8 -*-
{
    'name': "Hồ sơ trình ký",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "TIGO",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'data_master'
    ],

    # always loaded
    'data': [
        'wizard/popup_cmt.xml',
        'views/ho_so_trinh_ky.xml',
        'views/trinhky_chitiet.xml',
        'views/mau_so_trinh_ky.xml',
        'security/hstk_security.xml',
        'security/ir.model.access.csv',
    ],
}
