from django.test import TestCase
from contact.forms import ContatoForm


class ContactFormTest(TestCase):
    def setUp(self):
        self.form = ContatoForm()

    def test_has_form(self):
        expected = ['name', 'phone', 'email', 'message']
        self.assertSequenceEqual(expected, list(self.form.fields))
