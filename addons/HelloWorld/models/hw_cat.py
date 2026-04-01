from odoo import models, fields, api
from odoo.models import Constraint
from odoo.exceptions import ValidationError

class HelloWorldCategory(models.Model):
    _name = "sh.hello.world.category"
    _description = "Categoria"
    name = fields.Char(string="Nombre", required=True)