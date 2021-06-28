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

    'depends': ['account'],

    'data': [
        'security/ir.model.access.csv',

        'views/account_menuitem_inherit.xml',
        'views/account_move_view_inherit.xml',

    ],
    'demo': [
        'demo/demo.xml',
    ],
}
