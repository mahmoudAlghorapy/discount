# -*- coding: utf-8 -*-
{
    'name': "Discount",

    'summary': """
        Discount in po """,

    'description': """
        Discount in po
    """,
    'author': "My Company",
    'category': 'Uncategorized',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase'],

    # always loaded
    'data': [

        'views/po_line_discount.xml',
        'views/purchase_order_inherit.xml',

    ],
}
