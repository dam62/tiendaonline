# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import date
from dateutil.relativedelta import *

def validar_dni(dni):

    dni = dni.upper().strip()

    if len(dni) != 9:
        return False

    LETRAS_DNI = 'TRWAGMYFPDXBNJZSQVHLCKE'

    cuerpo = dni[:-1]
    letra_introducida = dni[-1]

    if cuerpo[0] in 'XYZ':
        mapeo_nie = {'X': '0', 'Y': '1', 'Z': '2'}
        cuerpo = mapeo_nie[cuerpo[0]] + cuerpo[1:]

    if not cuerpo.isdigit() or len(cuerpo) != 8:
        return False

    numero = int(cuerpo)

    posicion_letra = numero % 23
    letra_calculada = LETRAS_DNI[posicion_letra]

    return letra_introducida == letra_calculada

class Productos(models.Model):
    _name = 'tiendaonline.producto'
    _description = 'Define los atributos de un producto'
    _rec_name = 'nombreProducto'

    # Atributos
    nombreProducto = fields.Char(string='Nombre producto', required=True)
    tipoProducto = fields.Selection([('comida', 'Comida'),('cocina', 'Cocina'),
    ('ropa','Ropa'),('limpieza','Limpieza'),('bebida','Bebida'),('tecnologia','Tecnologia')], required=True, string="Tipo de producto")
    cantidadProducto = fields.Integer(string='Cantidad', required=True)

    # Relación de tablas
    pedidos_ids = fields.Many2many('tiendaonline.pedido', string='Pedidos')

    # Validaciones
    @api.constrains('cantidadProducto')
    def check_precio(self):
        if self.cantidadProducto <= 0:
            raise exceptions.ValidationError("Tiene que haber, al menos, un producto")

    @api.constrains('cantidadProducto')
    def _check_cantidad_logica(self):
        for producto in self:
            if producto.cantidadProducto > 50:
                raise exceptions.ValidationError("La cantidad del producto no puede superar 50 unidades.")


class Clientes(models.Model):
    _name = 'tiendaonline.cliente'
    _description = 'Define los atributos de un cliente'
    _rec_name = 'nombreCliente'

    # Atributos
    dniCliente = fields.Char(string='DNI cliente', required=True)
    nombreCliente = fields.Char(string='Nombre cliente', required=True)
    apellidosCliente = fields.Char(string='Apellidos cliente', required=True)
    correoCliente = fields.Char(string='Correo del cliente', required=True)

    # Relación de tablas
    pedido_ids = fields.One2many('tiendaonline.pedido', 'cliente_id', string='Pedidos')

    # Validaciones
    @api.constrains('dniCliente')
    def _check_dni(self):
        for cliente in self:
            okDNI = validar_dni(cliente.dniCliente)
            if (not okDNI):
                raise exceptions.ValidationError("El DNI introducido no es correcto")

class Pedidos(models.Model):
    _name = 'tiendaonline.pedido'
    _description = 'Define los atributos de un pedido'
    _rec_name = 'infoPedido'

    # Atributos
    infoPedido = fields.Char(string='Información del pedido', required=True)
    fechaPedido = fields.Date(string='Fecha pedido', required=True)
    importeTotal = fields.Float(string='Importe pedido', required=True)

    # Relación de tablas
    cliente_id = fields.Many2one('tiendaonline.cliente', string='Cliente')
    producto_ids = fields.Many2many('tiendaonline.producto', string='Productos')

    # Validaciones
    @api.constrains('fechaPedido')
    def _check_fecha_pedido(self):
        hoy = date.today()
        for pedido in self:
            if pedido.fechaPedido < hoy:
                raise exceptions.ValidationError("La fecha tiene que ser mayor que la fecha actual")

    @api.constrains('importeTotal')
    def _check_importe_positivo(self):
        for pedido in self:
            if pedido.importeTotal <= 0:
                raise exceptions.ValidationError("El importe no debe ser menor o igual a 0")

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

