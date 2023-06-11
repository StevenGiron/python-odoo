from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Candidate(models.Model):
    _inherit = 'res.partner'

    is_candidate = fields.Boolean(string='¿Es estudiante?')
    @api.constrains('vat')
    def _check_documento_unico(self):
        for candidate in self:
            if candidate.vat and self.search([('id', '!=', candidate.id), ('vat', '=', candidate.vat)]):
                raise ValidationError('El nro. de identificacion debe ser unico')


    @api.onchange('is_student')
    def _onchange_is_student(self):
        if self.is_student:
            self.is_candidate = False
