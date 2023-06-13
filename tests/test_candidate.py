from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestCandidate(TransactionCase):

    def setUp(self):
        super(TestCandidate, self).setUp()

        self.candidate1 = self.env['res.partner'].create({
            'name': 'Candidate 1',
            'is_candidate': True,
            'vat': '123456789'
        })
        self.candidate2 = self.env['res.partner'].create({
            'name': 'Candidate 2',
            'is_candidate': True,
            'vat': '987654321'
        })

    def test_check_documento_unico(self):
        with self.assertRaises(ValidationError):
            self.env['res.partner'].create({
                'name': 'Candidate 3',
                'is_candidate': True,
                'vat': '123456789'
            })

    def test_onchange_is_candidate(self):

        self.candidate1.is_candidate = True
        self.assertFalse(self.candidate1.is_student)

        self.candidate1.is_candidate = False
        self.assertTrue(self.candidate1.is_student)

    def test_add_vote(self):

        self.assertEqual(self.candidate1.number_votes, 0)

        self.candidate1.add_vote()
        self.assertEqual(self.candidate1.number_votes, 1)

    def test_compute_num_votes(self):
        vote1 = self.env['vote'].create({'candidate': self.candidate1.id})
        vote2 = self.env['vote'].create({'candidate': self.candidate1.id})
        vote3 = self.env['vote'].create({'candidate': self.candidate1.id})

        self.candidate1.compute_num_votes(self.candidate1.id)
        self.assertEqual(self.candidate1.number_votes, 3)