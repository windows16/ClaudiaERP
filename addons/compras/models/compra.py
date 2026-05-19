from odoo import models, fields, api


class Compra(models.Model):
    _name = 'iv.compra'
    _description = 'Compra'
    _rec_name = 'name'

    name = fields.Char(string='Número', default='Nueva Compra', readonly=True)
    fecha = fields.Datetime(string='Fecha', default=fields.Datetime.now, required=True)
    proveedor_id = fields.Many2one('iv.proveedor', string='Proveedor', required=True)
    detalle_ids = fields.One2many('iv.detalle.compra', 'compra_id', string='Detalle')
    total = fields.Float(string='Total', compute='_compute_total', store=True, digits=(10, 2))
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('recibida', 'Recibida'),
        ('cancelada', 'Cancelada'),
    ], string='Estado', default='borrador')

    @api.depends('detalle_ids.subtotal')
    def _compute_total(self):
        for rec in self:
            rec.total = sum(rec.detalle_ids.mapped('subtotal'))

    def action_recibir(self):
        for rec in self:
            rec.estado = 'recibida'
            # Aumentar stock
            for detalle in rec.detalle_ids:
                detalle.producto_id.stock += detalle.cantidad
                self.env['iv.movimiento.inventario'].create({
                    'producto_id': detalle.producto_id.id,
                    'tipo_movimiento': 'entrada',
                    'cantidad': detalle.cantidad,
                    'referencia': rec.name,
                })

    def action_cancelar(self):
        for rec in self:
            rec.estado = 'cancelada'


class DetalleCompra(models.Model):
    _name = 'iv.detalle.compra'
    _description = 'Detalle de Compra'

    compra_id = fields.Many2one('iv.compra', string='Compra', ondelete='cascade')
    producto_id = fields.Many2one('iv.producto', string='Producto', required=True)
    cantidad = fields.Integer(string='Cantidad', default=1)
    costo_unitario = fields.Float(string='Costo Unitario', digits=(10, 2))
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True, digits=(10, 2))

    @api.onchange('producto_id')
    def _onchange_producto(self):
        if self.producto_id:
            self.costo_unitario = self.producto_id.precio_compra

    @api.depends('cantidad', 'costo_unitario')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.cantidad * rec.costo_unitario
