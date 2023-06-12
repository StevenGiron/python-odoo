from odoo import http
from odoo.http import request
from odoo.exceptions import ValidationError


class Voting(http.Controller):
    @http.route('/votaciones', type='http', auth='public', website=True)
    def voting_web_form(self, **post):

        # Obtener el id del proceso de votacion
        voting_process_id = int(post.get('voting_process', 8))

        # Obtener los procesos de votacion
        voting_processes = request.env['voting.process'].sudo().search([('state', '=', 'en proceso')])

        voting_process = request.env['voting.process'].browse(voting_process_id)

        candidates = voting_process.candidates

        # Obtener todos los paises
        countries = request.env['res.country'].sudo().search([])

        return http.request.render('universidad.voting_website_template', {'countries': countries,
                                                                           'candidates': candidates,
                                                                           'voting_processes': voting_processes,
                                                                           })

    @http.route('/website/voting', type='http', auth='public', csrf=False, website=True)
    def vote(self, **post):

        # Obtener el id del pais desde el que se esta votando
        from_country_id = int(post.get('country'))

        # Obtener id del proceso al que se votara
        voting_process_id = int(post.get('voting_process', 8))

        # Obtener el proceso de votacion al que se votara
        voting_process = request.env['voting.process'].browse(voting_process_id)

        # Validar la disponbilidad del proceso de votacion desde otro pais
        voting_process.check_datetime_availability(from_country_id)

        # Validar el estado de la votacion
        voting_process.check_state_()

        # Obtener documento del votante
        vat = int(post.get('vat'))

        # Obtener el estudiante que esta votando
        student = request.env['res.partner'].sudo().search(['&', ('vat', '=', vat), ('is_student', '=', True)])

        # Validar las condiciones del estudiante
        if student:
            student.check_voted_()
            student.write({'voted': True})
        else:
            raise ValidationError('Debe ser estudiante para poder votar')

        # Obtener el id del candidato
        candidate_id = int(post.get('candidate'))

        # Obtener al candidato
        candidate = request.env['res.partner'].sudo().search(['&', ('id', '=', candidate_id), ('is_candidate', '=', True)])

        if candidate:
            candidate.add_vote()
            candidate.write({'number_votes': candidate.number_votes_})
        else:
            raise ValidationError('Seleccione un candidato')

        return http.request.redirect('/votaciones')

