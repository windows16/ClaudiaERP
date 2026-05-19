{
    'name': 'Compras',
    'version': '17.0.1.0.0',
    'category': 'Purchase',
    'summary': 'Gestión de compras y proveedores',
    'description': 'Módulo para gestión de proveedores y órdenes de compra.',
    'author': 'Custom',
    'depends': ['base', 'inventario'],
    'data': [
        'security/ir.model.access.csv',
        'views/proveedores_views.xml',
        'views/compras_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
