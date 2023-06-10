from odoo import api, fields, models


class VotingProcess(models.Model):
    _name = 'voting.process'

    description = fields.Char(string='Descripcion de la votacion', required=True)
    start_date = fields.Datetime(string='Fecha de inicio', required=True)
    end_date = fields.Datetime(string='Fecha de finalizacion', required=True)
    candidates = fields.Many2many('res.partner', domain=[('is_student', '=', False)])
    state = fields.Char(default='borrador')
    country = fields.Many2many('res.country', string='Pais', required=True)
    vote = fields.One2many('vote', 'id')

    @api.constrains('start_date', 'end_date')
    def _check_state(self):
        if self.start_date >= self.end_date:
            self.state = 'cerrada'
        else:
            self.state = 'en proceso'

