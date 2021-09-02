from odoo import api, fields, models

class TentArticle(models.Model):

    _name = "tent.article"
    _description = "New Article Tent"

    article_name = fields.Char(string='Nom', required=True, tracking=True)
    tent_width = fields.Integer(string='Largeur de la tente', required=True)
    armatures_amount = fields.Integer(string = 'Nombre d\'armatures disponibles', required=True)
    pignons_amount = fields.Integer(string = 'Nombre de pignons disponibles', required=True)
    note = fields.Text(string='Description')
    image = fields.Binary(string="Image")
    amount_available = fields.Integer(string='Quantité encore possible à sous-louer', compute='_compute_appointment_count')
    active = fields.Boolean(string="Active", default=True)
    article_composed_ids = fields.One2many('product.template', 'articles_tent_id', string="Articles composants")


        
