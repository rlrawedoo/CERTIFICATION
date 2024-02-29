# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2011 CCI Connect asbl (http://www.cciconnect.be) All Rights Reserved.
#                       Philmer <philmer@cciconnect.be>

{
    'name': 'Certification',
    'version': '1.0',
    'category': 'Tools',
    'description': """
Certification.
======================
""",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/certification.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
