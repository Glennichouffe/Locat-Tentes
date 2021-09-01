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
    'data': [
    'reports/sale_order_detail.xml',
    'reports/report_button.xml'
    ],
    'active' : 'False',
    # data files containing optionally loaded demonstration data
    'demo': [],
}
