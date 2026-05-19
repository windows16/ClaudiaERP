from odoo import models, fields, api


class Venta(models.Model):
    _name = 'iv.venta'
    _description = 'Venta'
    _rec_name = 'name'

    name = fields.Char(string='Número', default='Nueva Venta', readonly=True)
    fecha = fields.Datetime(string='Fecha', default=fields.Datetime.now, required=True)
    cliente_id = fields.Many2one('iv.cliente', string='Cliente', required=True)
    detalle_ids = fields.One2many('iv.detalle.venta', 'venta_id', string='Detalle')
    subtotal = fields.Float(string='Subtotal', compute='_compute_totales', store=True, digits=(10, 2))
    impuesto = fields.Float(string='Impuesto (12%)', compute='_compute_totales', store=True, digits=(10, 2))
    total = fields.Float(string='Total', compute='_compute_totales', store=True, digits=(10, 2))
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ], string='Estado', default='borrador')

    @api.depends('detalle_ids.subtotal')
    def _compute_totales(self):
        for rec in self:
            rec.subtotal = sum(rec.detalle_ids.mapped('subtotal'))
            rec.impuesto = rec.subtotal * 0.12
            rec.total = rec.subtotal + rec.impuesto

    def action_confirmar(self):
        for rec in self:
            rec.estado = 'confirmada'
            # Descontar stock
            for detalle in rec.detalle_ids:
                detalle.producto_id.stock -= detalle.cantidad
                self.env['iv.movimiento.inventario'].create({
                    'producto_id': detalle.producto_id.id,
                    'tipo_movimiento': 'salida',
                    'cantidad': detalle.cantidad,
                    'referencia': rec.name,
                })

    def action_cancelar(self):
        for rec in self:
            if rec.estado == 'confirmada':
                for detalle in rec.detalle_ids:
                    detalle.producto_id.stock += detalle.cantidad
            rec.estado = 'cancelada'


class DetalleVenta(models.Model):
    _name = 'iv.detalle.venta'
    _description = 'Detalle de Venta'

    venta_id = fields.Many2one('iv.venta', string='Venta', ondelete='cascade')
    producto_id = fields.Many2one('iv.producto', string='Producto', required=True)
    cantidad = fields.Integer(string='Cantidad', default=1)
    precio_unitario = fields.Float(string='Precio Unitario', digits=(10, 2))
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True, digits=(10, 2))

    @api.onchange('producto_id')
    def _onchange_producto(self):
        if self.producto_id:
            self.precio_unitario = self.producto_id.precio_venta

    @api.depends('cantidad', 'precio_unitario')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.cantidad * rec.precio_unitario
