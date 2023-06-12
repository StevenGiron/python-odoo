from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Student(models.Model):
    _inherit = 'res.partner'

    career = fields.Char(string='Carrera universitaria')
    campus_id = fields.Many2one('campus', string='Campus Universitario')
    is_student = fields.Boolean(string='¿Es estudiante?', default=False)
    voted = fields.Boolean(default=False)

    @api.onchange('is_student')
    def _onchange_is_student(self):
        if self.is_student:
            self.is_candidate = False
        else:
            self.is_candidate = True

    @property
    def voted_(self):
        return self.voted

    @voted_.setter
    def voted_(self, value):
        self.voted = value

    def check_voted_(self):
        if self.voted_:
            raise ValidationError('Ya has votado anteriormente')

