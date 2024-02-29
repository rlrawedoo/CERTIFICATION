# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class CertificationQuestion(models.Model):
    _name = "certification.question"
    _description = 'Certificaction Question'
    _order = "name"

    name = fields.Text(string='Question', index=True)
    answer = fields.Image("Answer")
    category = fields.Selection(
        selection=[
            ('intro', 'Introducción'),
            ('website', 'Sitio Web'),
            ('ecommerce', 'Commercio Electrónico'),
            ('survey', 'Encuesta'),
            ('information', 'Información'),
            ('marketing', 'Marketing'),
            ('crm', 'CRM'),
            ('sales', 'Ventas'),
            ('purchase', 'Compras'),
            ('project', 'Proyecto'),
            ('timesheet', 'Hojas de Horas'),
            ('account', 'Contabilidad'),
            ('inventory', 'Inventario'),
            ('mrp', 'MRP'),
            ('hr', 'HR'),
            ('calc', 'Hoja de Cálculo'),
            ('studio', 'Studio'),
        ],
        string="App"
    )