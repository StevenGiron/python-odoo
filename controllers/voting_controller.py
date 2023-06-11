from odoo import http
from odoo.http import request


class Voting(http.Controller):
    @http.route('/votaciones', type='http', auth='public', website=True)
    def voting_web_form(self, **kw):
        countries = request.env['res.country'].sudo().search([])
        candidates = request.env['res.partner'].sudo().search([('is_candidate', '=', True)])
        return http.request.render('universidad.voting_website_template', {'countries': countries,
                                                                           'candidates': candidates})
