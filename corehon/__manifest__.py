# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Corecash App',
    'version': '12.0.1.0.0',
    "author": "Vauxoo",
    "license": "LGPL-3",
    'category': 'Hidden',
    'summary': 'Corecash App for customizations',
    'depends': [
        'sale_management',
        'account_accountant',
        'account_reports',
        'stock',
        'account_invoice_production_lot',
    ],
    'data': [
        'views/account_invoice_view.xml',
        'reports/layout_invoice.xml',
        'reports/layout_creditnote.xml',
        'reports/layout.xml',
        'reports/report.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': True,
}
