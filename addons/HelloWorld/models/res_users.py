from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    frase_personal = fields.Char(string="Frase Personal")