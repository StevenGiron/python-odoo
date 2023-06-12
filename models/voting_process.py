from odoo import api, fields, models, _
from odoo.http import request
# from tools.get_datetime_country import get_datetime_country_


class VotingProcess(models.Model):
    _name = 'voting.process'

    description = fields.Char(string='Descripcion de la votacion', required=True)
    start_date = fields.Datetime(string='Fecha de inicio', required=True)
    end_date = fields.Datetime(string='Fecha de finalizacion', required=True)
    candidates = fields.Many2many('res.partner', string='Candidates', required=True,
                                  domain=['&', ('is_candidate', '=', True), ('is_candidate', '!=', None)])
    state = fields.Char(default='borrador')
    country = fields.Many2one('res.country', string='Pais', required=True)
    vote = fields.One2many('vote', 'id')

    @api.constrains('start_date', 'end_date')
    def _compute_state(self):
        if self.start_date >= self.end_date:
            self.state = 'cerrada'
        else:
            self.state = 'en proceso'

    def check_state_(self):
        if self.state == 'cerrada':
            raise ValidationError('Esta votacion esta cerrada')
    def get_candidates(self):
        return self.candidates

    def check_datetime_availability(self, country_id):
        # Obtener el pais desde el que se esta votando
        from_country = request.env['res.country'].sudo().search([('id', '=', country_id)]).code

        #country_datetime = get_datetime_country_(from_country)

        #if country_datetime > self.end_date:
         #   raise ValidationError('Esta votacion esta cerrada para su pais')

