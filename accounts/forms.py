from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

attrs = {'class':'form-control'}
class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs=attrs))
    password = forms.CharField(widget=forms.PasswordInput(attrs=attrs),label=_('Password'))


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs=attrs),label=_('First Name'))
    last_name = forms.CharField(widget=forms.TextInput(attrs=attrs),label=_('Last Name'))
    username = forms.CharField(widget=forms.TextInput(attrs=attrs),label=_('Username'))
    email = forms.EmailField(widget=forms.EmailInput(attrs=attrs),label=_('Email'))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs),label=_('Password'),strip=False,)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs),label=_('Password Confirmation'),strip=False,)



    class Meta(UserCreationForm.Meta):
        fields = ('first_name', 'last_name', 'username', 'email')



class ProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs=attrs),
            'last_name': forms.TextInput(attrs=attrs),
            'email': forms.EmailInput(attrs=attrs),
        }