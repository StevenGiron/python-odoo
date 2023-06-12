from odoo import api, fields, models, _
from odoo.http import request
from odoo.exceptions import ValidationError

import pytz
from datetime import datetime



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

    def get_datetime_country_(self, country):
        try:
            tz_by_country = pytz.country_timezones[country]

            tz_country = pytz.timezone(tz_by_country[0])

            current_datetime = datetime.now(tz_country)
            return current_datetime.strftime('%Y-%m-%d %H:%M:%S')
        except KeyError:
            return "País no válido o no se encontró información sobre la zona horaria."

    def check_datetime_availability(self, country_id):
        # Obtener el pais desde el que se esta votando
        from_country = request.env['res.country'].sudo().search([('id', '=', country_id)]).code

        country_datetime = self.get_datetime_country_(from_country)

        if country_datetime > self.end_date:
            raise ValidationError('Esta votacion esta cerrada para su pais')

