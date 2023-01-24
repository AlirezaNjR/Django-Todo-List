from django import forms
from django.contrib.auth.models import User
class SignUpForm(forms.Form):
    username = forms.CharField(max_length=32,required=True,label='نام کاربری')
    first_name = forms.CharField(max_length=32,required=False,label='نام')
    last_name = forms.CharField(max_length=32,required=False,label='نام خانوادگی')
    email = forms.EmailField(max_length=254,required=False,label='ایمیل')
    password = forms.CharField(widget=forms.PasswordInput,required=True,label='رمز عبور')
    c_password = forms.CharField(widget=forms.PasswordInput,required=True,label='تکرار رمز عبور')
    
    def clean_password(self):
        text = self.cleaned_data['password']
        if len(text) >= 8:
            return text
        else:
            raise forms.ValidationError('رمز عبور کوتاه است')
        
    # def clean_c_password(self):
    #     c_password = self.cleaned_data['c_password']
    #     password = self.cleaned_data['password']
    #     if password == c_password:
    #         return c_password
    #     else:
    #         raise forms.ValidationError('رمز عبور با تکرارش یکسان نیست')