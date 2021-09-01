# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PriceWithInstallation(models.Model):
    _inherit = "product.template"

    price_with_installation = fields.Char(string='Prix avec l\'installation')
