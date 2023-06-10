from odoo import api, fields, models


class Student(models.Model):
    _inherit = 'res.partner'

    career = fields.Char(string='Carrera universitaria')
    campus_id = fields.Many2one('campus', string='Campus Universitario')
    is_student = fields.Boolean(string='¿Es estudiante?')
    voted = fields.Boolean(default=False)
