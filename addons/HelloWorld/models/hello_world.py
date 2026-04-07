from odoo import models, fields, api # type: ignore
from odoo.models import Constraint # type: ignore
from odoo.exceptions import ValidationError # type: ignore

class HelloWorld(models.Model):
    _name = "sh.hello.world"
    _description = "Modelo Principal"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Nombre", required=True, tracking=True)
    boolean_field = fields.Boolean(string="Activo", default=False)
    description_larga = fields.Text(string="Descripcion", tracking=True)
    
    # Campo Many2one: Relación con el usuario responsable
    user_id = fields.Many2one('res.users', string='Responsable', default=lambda self: self.env.user)
    
    # Campo Relacionado: Trae la frase personal del usuario responsable
    user_phrase = fields.Char(
    related='user_id.frase_personal', 
    string="Frase del Responsable",
    readonly=True
    )

    # RELACIONES
    category_id = fields.Many2one('sh.hello.world.category', string="Categoria")
    tag_ids = fields.Many2many('sh.hello.world.tag', string='Etiquetas')

    # RESTRICCIONES
    _name_unique = Constraint(
        'unique(name)', 
        '¡El nombre debe ser único!'
    )

    # Definimos los estados posibles
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('locked', 'Bloqueado'),
    ], string='Estado', default='draft', tracking=True)

    # Función para bloquear
    def action_lock(self):
        self.state = 'locked'

    # Función para volver a borrador (desbloquear)
    def action_unlock(self):
        self.state = 'draft'

    @api.constrains('name')
    def _check_name_length(self):
        for record in self:
            if record.name and len(record.name) < 3:
                raise ValidationError("El nombre debe tener al menos 3 caracteres.")

    # 1. Campo Computado: Cuenta cuántas etiquetas hay
    tag_count = fields.Integer(string="Número de Etiquetas", compute="_compute_tag_count")

    @api.depends('tag_ids')
    def _compute_tag_count(self):
        for record in self:
            record.tag_count = len(record.tag_ids)

    # 2. Onchange: Si marcamos el boolean, ponemos un nombre por defecto
    @api.onchange('boolean_field')
    def _onchange_boolean_field(self):
        if self.boolean_field and not self.name:
            self.name = "Registro Automático"

    # 3. Acción de Objeto: Un botón para limpiar la descripción
    def action_clear_description(self):
        self.description_larga = ""
        # Opcional: devolver un aviso o simplemente nada
        return True
