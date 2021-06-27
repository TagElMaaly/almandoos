# -*- coding: utf-8 -*-
{
    'name': "account_enhancement",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Tag ElMaaly",
    'website': "http://www.yourcompany.com",

    'category': 'Accounting/Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_menuitem_inherit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
