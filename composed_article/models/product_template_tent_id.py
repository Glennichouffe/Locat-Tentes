from odoo import api, fields, models

class ProductTemplateTentId(models.Model):

    _inherit = 'product.template'

    articles_tent_id = fields.Many2one('tent.article', 'TentID')
   
