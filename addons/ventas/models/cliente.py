from odoo import models, fields


class Cliente(models.Model):
    _name = 'iv.cliente'
    _description = 'Cliente'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    telefono = fields.Char(string='Teléfono')
    correo = fields.Char(string='Correo')
    direccion = fields.Char(string='Dirección')
    fecha_registro = fields.Datetime(string='Fecha de Registro', default=fields.Datetime.now)

    venta_ids = fields.One2many('iv.venta', 'cliente_id', string='Ventas')
    total_ventas = fields.Integer(string='Total Ventas', compute='_compute_total_ventas')

    def _compute_total_ventas(self):
        for rec in self:
            rec.total_ventas = len(rec.venta_ids)
