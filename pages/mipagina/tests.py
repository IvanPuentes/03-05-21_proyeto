from django.test import SimpleTestCase


# Create your tests here.
#agregar diferentes pruebas al archivo test
class SimpleTestCase(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('')
        self.assertEqual(response.status_code,200)
   