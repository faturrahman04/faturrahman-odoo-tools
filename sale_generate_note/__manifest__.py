# -*- coding: utf-8 -*-
{
    'name': "Sale Generate Note",
    'summary': "Improve your sales documentation.",
    'author': "Faturrahman Alfarisi",
    'website': "https://faturrahmanalfarisi.vercel.app/",
    'category': 'Customizations',
    'version': '1.0',
    'depends': ['base', 'sale'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
        'views/mail_templates_sale.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license' : 'LGPL-3'
}

