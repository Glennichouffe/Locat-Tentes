# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PriceSaleOrder(models.Model):
    _inherit = "sale.order.line"

    price_with_installation = fields.Float(string='Prix avec l\'installation')
