from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Candidate(models.Model):
    _inherit = 'res.partner'


    @api.constrains('vat')
    def _check_documento_unico(self):
        for candidate in self:
            if candidate.vat and self.search([('id', '!=', candidate.id), ('vat', '=', candidate.vat)]):
                raise ValidationError('El nro. de identificacion debe ser unico')
