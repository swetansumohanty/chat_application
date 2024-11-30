from django.test import SimpleTestCase
from a_user.forms import SignUpForm

class TestForms(SimpleTestCase):
    """
    testing forms.
    """
    def test_form_with_valid_data(self):
        form = SignUpForm(data={
            'username':'rohit2',
            'first_name':'grurnath',
            'last_name': 'sharma',
            'email':'rohit@gmail.com',
            'mobile': 8018898592,
            'password':'rohit@32',
            'password_confirm':'rohit@32',
            'agree':True
        })
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_form_with_no_data(self):
        form = SignUpForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),6)

    def test_form_with_partial_data(self):
        form = SignUpForm(data={
            "username":"sri4",
            "first_name":"Ram",
            "mobile":9853167634,
            "password":"sriram32",
            "password_confirm":"sriram32"
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),2)


    def test_form_email_without_symbols(self):
        form=SignUpForm(data={
            'username':'rohit3',
            'first_name':'grurnath',
            'last_name': 'sharma',
            'email':'rohitgmail com',    # if not ("@"and ".") or " " in email attributes
            'mobile': 8018898592,
            'password':'rohit@321',
            'password_confirm':'rohit@321',
            'agree':True
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),3)

    def test_form_password(self):
        form=SignUpForm(data={
            'username':'rohit3',
            'first_name':'grurnath',
            'last_name': 'sharma',
            'email':'rohit@gmail.com',    
            'mobile': 8018898592,
            'password':'rohit@321',
            'password_confirm':'rohit@324',   # if 'password' and 'confirm password' mismatch and len(password) !=8
            'agree':True
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),2)

        