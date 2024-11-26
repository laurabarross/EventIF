from django.test import TestCase
from django.core import mail

class ContactPostValid(TestCase):
    def setUp(self):
        data = dict(name='Laura', phone='53-12345-6789', email='laura@gmail.com', message='bom dia')
        self.client.post('/contato/', data)
        self.email = mail.outbox[0]

    def test_contact_email_subject(self):
        expect = 'Confirmação de contato.'
        self.assertEqual(expect, self.email.subject)

    def test_contact_email_from(self):
        expect = 'laura@gmail.com'
        self.assertEqual(expect, self.email.from_email)

    def test_contact_email_to(self):
        expect = ['laura@gmail.com', 'contato@eventif.com.br']
        self.assertEqual(expect, self.email.to)

    def test_contact_email_body(self):
        contents = (
            'Laura',
            '53-12345-6789',
            'laura@gmail.com',
            'bom dia'
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
