from django.test import TestCase

class ViewTestCase(TestCase):
    """
    testing views.
    """
    def test_view(self):
        """
        Test login view
        """
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'a_user/login.html')

    def test_view2(self):
        """
        sign_up view
        """
        response = self.client.get('/sign_up/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'a_user/signup.html')

    def test_view3(self):
        """
        profile view
        """
        response = self.client.get('/u_profile/')
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/')
    
    def test_view4(self):
        """
        logout view
        """
        response = self.client.get('/u_logout/')
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/')