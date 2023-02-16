# -*- coding: utf-8 -*-
{
    'name': "Data Master",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "THG",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base'
    ],

    # always loaded
    'data': [
        'views/frequency_truong.xml',
        'views/applied_learning.xml',
        'views/applied_subjects.xml',
        'views/file.xml',
        'views/object.xml',
        'views/school.xml',
        'views/education_truong.xml',
        'views/school_level_truong.xml',
        'views/applicable_type.xml',
        'security/ir.model.access.csv',
    ],
}
