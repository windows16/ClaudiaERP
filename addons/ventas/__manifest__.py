{
    'name': 'Ventas',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'Gestión de ventas y clientes',
    'description': 'Módulo para gestión de clientes y órdenes de venta.',
    'author': 'Custom',
    'depends': ['base', 'inventario'],
    'data': [
        'security/ir.model.access.csv',
        'views/clientes_views.xml',
        'views/ventas_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
