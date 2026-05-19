from odoo import models, fields, api


class Producto(models.Model):
    _name = 'iv.producto'
    _description = 'Producto'
    _rec_name = 'nombre'

    codigo = fields.Char(string='Código', required=True)
    nombre = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    precio_compra = fields.Float(string='Precio de Compra', digits=(10, 2))
    precio_venta = fields.Float(string='Precio de Venta', digits=(10, 2))
    stock = fields.Integer(string='Stock Actual', default=0)
    stock_minimo = fields.Integer(string='Stock Mínimo', default=0)
    categoria_id = fields.Many2one('iv.categoria', string='Categoría')
    proveedor_id = fields.Many2one('iv.proveedor', string='Proveedor')

    bajo_stock = fields.Boolean(string='Bajo Stock', compute='_compute_bajo_stock', store=True)

    @api.depends('stock', 'stock_minimo')
    def _compute_bajo_stock(self):
        for rec in self:
            rec.bajo_stock = rec.stock <= rec.stock_minimo
