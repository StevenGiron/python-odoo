from odoo import api, fields, models


class Vote(models.Model):
    _name = 'vote'

    candidate = fields.Many2one('res.partner', string='Candidato', domain=[('is_student', '=', False)])
    voting_process = fields.Many2one('voting.process')
