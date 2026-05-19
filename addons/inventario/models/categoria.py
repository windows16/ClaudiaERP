from odoo import models, fields


class Categoria(models.Model):
    _name = 'iv.categoria'
    _description = 'Categoría de Producto'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    descripcion = fields.Char(string='Descripción')

    producto_ids = fields.One2many('iv.producto', 'categoria_id', string='Productos')
