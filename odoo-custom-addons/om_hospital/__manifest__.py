# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital Management system',
    'version' : '13.0.1.0',
    'summary': 'Managing the hospital',
    'sequence': 15,
    'author': 'Almabud',
    'maintainer': 'Almabud',
    'description': """Hello to my custom module""",
    'category': 'Accounting/Accounting',
    'website': '',
    'images' : [],
    'depends' : ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}