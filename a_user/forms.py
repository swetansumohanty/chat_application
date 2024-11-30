from django import forms
import re

class SignUpForm(forms.Form):
    """
    Generate a user registration form.
    """    
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30,required=False)
    last_name = forms.CharField(max_length=30,required=False)
    email = forms.EmailField(max_length=30)
    mobile = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput,max_length=8)
    password_confirm = forms.CharField(widget=forms.PasswordInput,max_length=8,label="Password CNF")
    agree = forms.BooleanField(label_suffix="")

    def clean_username(self) -> str:
        """
        validate username.
        :return:str
        """
        user = self.cleaned_data['username']
        
        if any(char.isspace() for char in user):

            raise forms.ValidationError('username can not contain blank space')
        if not any(char.isdigit() for char in user):

            raise forms.ValidationError('username must contain a numeric digit')

        return user
             
    # mobile field validation
    def clean_mobile(self) -> int:
        """
        To validate mobile numbers.
        :return:int
        """
        mob = self.cleaned_data.get('mobile')
        if len(str(mob)) != 10:
            raise forms.ValidationError('at least 10 digits')

        # using regex
        obj = re.fullmatch('[6-9][0-9]{9}',str(mob))
        if obj == None:

            raise forms.ValidationError('Invalid number !, first digit must contain [6-9]')

        return mob
        
    # email validation
    def clean_email(self) -> str:
        """
        Validate email.
        :return:str
        """
        em = self.cleaned_data.get('email')
        # regex for email 
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        robj = re.fullmatch(regex, em)
        if robj is None:
                
            raise forms.ValidationError('enter a valid email address')
        
        return em

    # password validation
    def clean(self):
        """
        Validate password.
        :return: int
        """

        # representing the parent class 
        cleaned_data = super().clean()   

        pass1 = self.cleaned_data.get('password')
        pass2 = self.cleaned_data.get('password_confirm')
      
        if pass1 != pass2:

            raise forms.ValidationError('password mismatch'+'\n'+ 'sorry try again !')

