# -*- coding: utf-8 -*-

from datetime import datetime, date
from email.policy import default
from random import randint
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class bicycle(models.Model):
    _name = 'manbike61.bicycle'
    _description = 'A bicycle'

    name = fields.Char(string = "Modelo", readonly = False, required = True, help = "Modelo exacto de bicicleta sin fabricante")
    description = fields.Text(string = "Descripción")
    price = fields.Float(string = "Precio", required = True)
    inShop = fields.Date(string = "Entrada en tienda", default = lambda self: date.today())
    endShop = fields.Date(string = "Salida de tienda", default = lambda self: date.today())
    year = fields.Integer(string = "Año", default = 2021)
    single_chainring = fields.Boolean(string = "Mono plato", compute = "_set_single_chainring", store = True)
    photo = fields.Image(string = "Fotografía", max_width=400, max_height=400)

    chainring = fields.Integer(string = "Nº. de platos", default = 1)
    cassette = fields.Integer(string = "Nº. de piñones")
    speed = fields.Integer(string = "Nº de velocidades", compute = "_cal_speed", store = True)

    wheel = fields.Selection([('tipo26', '26\"'), ('tipo27', '27.5\"'), ('tipo29', '29\"')], string="Diámetro Rueda")

    manufacturer = fields.Many2one("manbike61.manufacturer", string = "Fabricantes")
    trader = fields.Many2many("manbike61.trader", related="manufacturer.trader", readonly=True)

    discount = fields.Boolean(string="Descuento aplicado", readonly=True, default=False)

    delivery = fields.Many2one("manbike61.delivery", string = "Paquetería")

    def calc_discount(self):
        for bike in self:
            if bike.discount != True:
                try:
                    bike.price = bike.price - (bike.price*0.1)
                    bike.discount = True
                except:
                    raise ValidationError("Discount can't be applied")
            else: 
                raise ValidationError("Discount can't be applied")

    @api.depends("chainring", "cassette")
    def _cal_speed(self):
        print("----->>>", type(self))
        print("----->>>", self)
        for bike in self: 
            print("\t ---->>>> ", bike.name)
            try: 
                bike.speed = bike.chainring * bike.cassette
            except:
                bike.speed = 1

    @api.depends("chainring")
    def _set_single_chainring(self):
        print("----->>>", type(self))
        print("----->>>", self)
        for bike in self: 
            print("\t ---->>>> ", bike.name)
            if(bike.chainring == 1):
                bike.single_chainring = True
            else :
                bike.single_chainring = False

    
class manufacturer(models.Model):
    _name = "manbike61.manufacturer"
    _description = "A manufacturer"

    name = fields.Char(string = "Fabricante")
    web = fields.Char(string = "Sitio web")

    bicycles = fields.One2many("manbike61.bicycle", "manufacturer", string="Bicicletas")
    trader = fields.Many2many("manbike61.trader", string = "Comerciales")

    trader_main = fields.One2many("manbike61.trader", "manuf_main", string = "Soy principal de: ")

class trader(models.Model):
    _name = 'manbike61.trader'
    _description = 'The Trade'

    name = fields.Char(string = "Comercial", required=True)
    phone = fields.Char(string = "Teléfono")
    dni = fields.Char(string = "DNI")

    manuf_main = fields.Many2one("manbike61.manufacturer", string = "Fabricante principal", compute = "_get_manuf_main", store = True)

    manufacturer = fields.Many2many("manbike61.manufacturer", string = "Fabricantes")

    @api.depends("manufacturer")
    def _get_manuf_main(self):
        for trade_current in self: 
            size_man = len(trade_current.manufacturer)
            if(size_man > 0):
                pos = randint(0, size_man-1)
                trade_current.manuf_main = trade_current.manufacturer[pos].id 
            else:
                trade_current.manuf_main = None

    @api.constrains("dni")
    def _validate_dni(self):
        DNI_REGEX = '^(\d{8})([A-Z])$'
        for trade_current in self: 
            if not trade_current.dni:
                print("----_validate_dni >>> DNI: Not Value")
            else: 
                print("----")
                '''if re.match(DNI_REGEX, trade_current.dni, re.I) == None:
                    raise ValidationError("DNI: Not valid")
                else: 
                    print("---_validate_dni >>> DNI: Valid")
                    if(self._exist_dni(trade_current.dni)):
                        raise ValidationError("DNI ALREADY EXISTS")
                    else:
                        print("----_validate_dni DNI: Valid and doesn't exist")'''
    _sql_constraints = [("dni_uniq", "unique(dni)", "DNI Alreay Exists!!!")]

    '''def _exist_dni(self, dni_to_check):
          all_trades= self.env['manbike61.trader'].search([])
          #print("-------_exist_dni>>>>>", type[all_trades])
          #print("-------_exist_dni>>>>>", all_trades)
          for at in all_trades:
               if at.dni == dni_to_check and at.id != self.id:
                    return True
          return False'''

    @api.constrains("phone")
    def _validate_phone(self):
        PHONE_REGEX = '^(6|7|8|9)([0-9]){8}$'
        for trade_current in self: 
            if not trade_current.phone:
                print("----_validate_phone >>> PHONE: Not Value")
            else: 
                if re.match(PHONE_REGEX, trade_current.phone) == None:
                    raise ValidationError("PHONE: Not valid")
                else: 
                    print("---_validate_phone >>> PHONE: Valid")
    
    '''@api.constrains("phone")
    def _validate_phone(self):
        PHONE_REGEX = '^(6|7|8|9)([0-9]){8}$'
        for trade_current in self:
            if not trade_current.phone:
                print("---validate PHONE not value")
            else:
                if re.match(PHONE_REGEX, trade_current.phone)==None:
                        raise ValidationError("PHONE: Not valid")
                else:
                        print("-----PHONE VALIDO")'''

class delivery(models.Model):
    _name = 'manbike61.delivery'
    _description = 'The Delivery'

    name = fields.Char(string = "Empresa", required=True)
    price = fields.Float(string = "Precio")
    shipment_days = fields.Integer(string = "Nº Días de Envío")



    #@api.constrains("phone")

        

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
