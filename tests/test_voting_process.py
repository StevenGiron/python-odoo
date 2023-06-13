from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
from datetime import datetime
from pytz import timezone


class TestVotingProcess(TransactionCase):

    def setUp(self):
        super(TestVotingProcess, self).setUp()

        # Crear registros de ejemplo
        self.country = self.env['res.country'].create({
            'name': 'Colombia',
        })
        self.candidate1 = self.env['res.partner'].create({
            'name': 'Candidate 1',
            'is_candidate': True,
            'country_id': self.country.id,
        })
        self.candidate2 = self.env['res.partner'].create({
            'name': 'Candidate 2',
            'is_candidate': True,
            'country_id': self.country.id,
        })
        self.voting_process = self.env['voting_process'].create({'description': 'Gobernador',
                                                            'start_date':  datetime.now(),
                                                            'end_date': datetime.now(),
                                                            'candidates': [(6, 0, [self.candidate1.id, self.candidate2.id])],
                                                            'country': self.country,
                                                            })

    def test_compute_state(self):
        self.voting_process._compute_state()
        self.asserEqual(self.state, 'cerrada')


    def check_state_(self):
        self.voting_process.state = 'cerrada'
        with self.assertRaises(ValidationError):
            self.voting_process.check_state_()

    def test_get_candidates(self):
        # Obtener los candidatos
        candidates = self.voting_process.get_candidates()

        # Verificar que los candidatos obtenidos coinciden con los candidatos creados en el setUp()
        self.assertEqual(len(candidates), 2)
        self.assertIn(self.candidate1, candidates)
        self.assertIn(self.candidate2, candidates)
