from  django import forms
from .models import Student

class StudentRegistration(forms.ModelForm):
    def special_chars(pwrd):
        if '@' not in pwrd and '$' not in pwrd and '^' not in pwrd and '&' not in pwrd and '_' not in pwrd:
            raise forms.ValidationError('Password must contain atleast one special character')
        return True
    password=forms.CharField(widget=forms.PasswordInput,required=True,validators=[special_chars])
    class Meta:
        model=Student
        fields=['name','email','password']
        error_messages={'name':{'required':'Enter Your Name'},
                        'email':{'required':'Enter Your Email'}}

