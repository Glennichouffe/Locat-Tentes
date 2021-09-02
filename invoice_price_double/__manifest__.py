{
    'name': "Second price for inventory",
    'version': '1.0',
    'depends': [
        'base',
        'stock', 
        'product'
    ],
    'author': "Glenn Crompton",
    'category': 'Renting',
    'description': """
   '
    """,
    # data files always loaded at installation
    'data': ['views/add_price.xml',
    'reports/invoice_price_extend.xml'],
    'active' : 'False',
    # data files containing optionally loaded demonstration data
    'demo': [],
}
