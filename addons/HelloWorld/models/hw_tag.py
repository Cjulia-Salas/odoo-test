from odoo import models, fields, api
from odoo.models import Constraint
from odoo.exceptions import ValidationError

class HelloWorldTag(models.Model):
    _name = "sh.hello.world.tag"
    _description = "Etiqueta"
    name = fields.Char(string="Nombre", required=True)
    color = fields.Integer(string="Color")