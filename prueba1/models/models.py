# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class prueba1(models.Model):
#     _name = 'prueba1.prueba1'
#     _description = 'prueba1.prueba1'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
