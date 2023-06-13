from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestStudent(TransactionCase):

    def setUp(self):
        super(TestStudent, self).setUp()
        self.student = self.env['res.partner'].create({
            'name': 'Alexis',
            'vat': '123',
        })

    def test_onchange_is_student(self):
        self.student.is_student = True
        self.assertFalse(self.student.is_candidate)

        self.student.is_student = False
        self.assertTrue(self.student.is_candidate)

    def test_check_voted(self):
        self.student.voted = True
        with self.assertRaises(ValidationError):
            self.student.check_voted_()

    def test_vat_property(self):
        self.assertEqual(self.student.vat_, '123')
