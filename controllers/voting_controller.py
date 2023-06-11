from odoo import http
from odoo.http import request


class Voting(http.Controller):

    @http.route('/votaciones', type='http', auth='public', website=True)
    def voting_web_form(self, **kw):
        return http.request.render('universidad.voting_website_template', {})
