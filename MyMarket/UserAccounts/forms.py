from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email', 'required':'true'}), label='', required=True)
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'First Name', 'required':'true'}), label='', required=True)
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'Last Name', 'required':'true'}), label='', required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None
            self.fields[field_name].label = ''

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Re-Enter Password'
