from django.test import TestCase

class ViewTestCase(TestCase):
    """
    class to test app.views
    """
    def test_one(self):
        response = self.client.get('/chat/aliens/')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'app/index.html')
