# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Productos(models.Model):
    _name = 'tiendaonline.producto'
    _description = 'Define los atributos de un producto'
    _rec_name = 'nombreProducto'

    # Atributos
    nombreProducto = fields.Char(string='Nombre producto', required=True)
    tipoProducto = fields.Selection([('f', 'Front-End'),('b', 'Back-End')], required=True, help='Tipo de producto')
    precioProducto = fields.Char(string='Precio del producto', required=True)

    # Relación de tablas
    pedidos_ids = fields.Many2many('tiendaonline.pedido', string='Pedidos')

class Clientes(models.Model):
    _name = 'tiendaonline.cliente'
    _description = 'Define los atributos de un cliente'
    _rec_name = 'nombreCliente'

    # Atributos
    dniCliente = fields.Char(string='DNI cliente', required=True)
    nombreCliente = fields.Char(string='Nombre cliente', required=True)
    apellidosCliente = fields.Char(string='Apellidos cliente', required=True)

    # Relación de tablas
    pedido_ids = fields.One2many('tiendaonline.pedido', string='Pedidos')

class Pedidos(models.Model):
    _name = 'tiendaonline.pedido'
    _description = 'Define los atributos de un pedido'
    _rec_name = 'nombrePedido'

    # Atributos
    nombrePedido = fields.Char(string='Nombre pedido', required=True)
    fechaPedido = fields.Date(string='Fecha pedido', required=True, default=fields.Date.today)
    importeTotal = fields.Char(string='Importe pedido', required=True)

    # Relación de tablas
    cliente_id = fields.Many2one('tiendaonline.cliente', string='Cliente')
    producto_ids = fields.Many2many('tiendaonline.producto', string='Productos')

# class tiendaonline(models.Model):
#     _name = 'tiendaonline.tiendaonline'
#     _description = 'tiendaonline.tiendaonline'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

