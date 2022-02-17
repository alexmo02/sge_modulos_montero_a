
from odoo import models, fields

class bicycle(models.Model):
    _name="bicycle.bike"

    name = fields.Char(string="Modelo", required=True, help="Introduce el modelo de la bicicleta")
    descripcion = fields.Text(string="Descripción", required=False, help="Introduce una descripción")
    precio = fields.Float(string="Precio", required=True, help="Introduce el precio de la bicicleta")