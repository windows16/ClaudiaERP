from odoo import models, fields


class MovimientoInventario(models.Model):
    _name = 'iv.movimiento.inventario'
    _description = 'Movimiento de Inventario'
    _order = 'fecha desc'

    producto_id = fields.Many2one('iv.producto', string='Producto', required=True)
    tipo_movimiento = fields.Selection([
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
        ('ajuste', 'Ajuste'),
    ], string='Tipo', required=True)
    cantidad = fields.Integer(string='Cantidad', required=True)
    fecha = fields.Datetime(string='Fecha', default=fields.Datetime.now)
    referencia = fields.Char(string='Referencia')
