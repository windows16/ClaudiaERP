{
    'name': 'Inventario',
    'version': '17.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Gestión de inventario, productos y categorías',
    'description': 'Módulo para gestión de productos, categorías de productos y movimientos de inventario.',
    'author': 'Custom',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/categorias_views.xml',
        'views/productos_views.xml',
        'views/movimientos_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
