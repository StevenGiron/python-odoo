from odoo import api, fields, models


class Campus(models.Model):
    _name = 'campus'

    name = fields.Char(string='Nombre del Campus', required=True)
    country = fields.Selection([
        ('belgica', 'Belgica'),
        ('colombia', 'Colombia'),
        ('venezuela', 'Venezuela'),
        ('argentina', 'Argentina'),
    ], string='Pais', required=True)
