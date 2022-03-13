# -*- coding: utf-8 -*-
{
    'name': "manbike61",

    'summary': """
        SGE Tema 6""",

    'description': """
        SGE Tema 6 - Paso a paso
    """,

    'author': "Alejandro Montero",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customization',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/manbike61_bicycle_report_template_html.xml',
        'report/manbike61_bicycle_report_template_pdf.xml',
        'report/manbike61_bicycle_report.xml',
        'data/data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
