from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Candidate(models.Model):
    _inherit = 'res.partner'

    is_candidate = fields.Boolean(string='¿Es estudiante?', default=False)
    number_votes = fields.Integer(string='Cantidad de Votos', compute='_onchange_vote_count')
    votes = fields.One2many('vote', 'id')

    @api.constrains('vat')
    def _check_documento_unico(self):
        for candidate in self:
            if candidate.vat and self.search([('id', '!=', candidate.id), ('vat', '=', candidate.vat)]):
                raise ValidationError('El nro. de identificacion debe ser unico')

    @api.onchange('is_candidate')
    def _onchange_is_candidate(self):
        if self.is_candidate:
            self.is_student = False
        else:
            self.is_student = True

    @api.onchange('votes')
    def _onchange_vote_count(self):
        for candidate in self:
            self.number_votes = self.env['vote'].search_count([('candidate', '=', candidate.id)])
