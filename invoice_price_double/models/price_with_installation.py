# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PriceWithInstallation(models.Model):
    _inherit = "product.template"

    price_with_installation = fields.Float(string='Prix avec l\'installation')
    has_second_price = fields.Boolean(string='A un prix d\'installation', default = True, compute='_compute_second_price')

    def _compute_second_price(self):
        for rec in self:
            if rec.price_with_installation > 0 :
                rec.has_second_price = True
            else : 
                rec.has_second_price = False