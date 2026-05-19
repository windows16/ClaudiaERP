from odoo import models, fields


class Proveedor(models.Model):
    _name = 'iv.proveedor'
    _description = 'Proveedor'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    telefono = fields.Char(string='Teléfono')
    correo = fields.Char(string='Correo')
    direccion = fields.Char(string='Dirección')

    compra_ids = fields.One2many('iv.compra', 'proveedor_id', string='Compras')
    producto_ids = fields.One2many('iv.producto', 'proveedor_id', string='Productos')
