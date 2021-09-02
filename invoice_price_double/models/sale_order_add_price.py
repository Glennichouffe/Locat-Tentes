# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PriceWithInstallation(models.Model):
    _inherit = "sale.order"

    price_with_installation = fields.Float(string='Prix avec l\'installation')
