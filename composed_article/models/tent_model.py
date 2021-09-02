from odoo import api, fields, models

class TentArticle(models.Model):

    _name = "tent.article"
    _description = "New Article Tent"

    article_name = fields.Char(string='Nom', required=True, tracking=True)
    tent_width = fields.Integer(string='Largeur de la tente', required=True)
    armatures_amount_total = fields.Integer(string = 'Nombre total d\armatures', required=True)
    pignons_amount_total = fields.Integer(string = 'Nombre total de pignons', required=True)
    note = fields.Text(string='Notes éventuelles')
    image = fields.Binary(string="Image")
    amount_available = fields.Integer(string='Quantité maximale de tentes possibles à louer', compute='_compute_maximum_quantity')
    active = fields.Boolean(string="Active", default=True)
    article_composed_ids = fields.One2many('product.template', 'articles_tent_id', string="Articles composants")
    price_week_without_installation = fields.Float('Prix pour une semaine de location sans installation',  required=True)
    price_week_with_installation = fields.Float('Prix pour une semaine de location avec installation',  required=True)
    rented_tents = fields.Integer('Nombre de tentes louées', readonly = True, default = 0)
    rented_armatures = fields.Integer('Nombre d\'armatures louées', readonly = True, default = 0)
    rented_pignons = fields.Integer('Nombre de pignons loués', readonly = True, default = 0)
    armatures_amount_available= fields.Integer(string = 'Armatures disponibles', default = lambda self: self.armatures_amount_total)
    pignons_amount_available = fields.Integer(string = 'Pignons disponibles', default = lambda self: self.pignons_amount_total)
    
    def _compute_maximum_quantity(self):
        for rec in self:
           rec.amount_available = rec.armatures_amount / 3

        
