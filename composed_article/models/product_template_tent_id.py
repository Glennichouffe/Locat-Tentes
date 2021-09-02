class ProductTemplateTentId(models.Model):

    _name = "product.template.many2one.field"
    _description = "Add many2one field for my module"
    _inherit = ['product.template']

    articles_tent_id = fields.many2one('tent.article', string='Tent ID')
   
