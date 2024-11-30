from django.test import TestCase

# Create your tests here.

class ViewTest(TestCase):

    def test_one(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code,200)
        print('response ----',response)
        self.assertTemplateUsed(response,'core/core.html')