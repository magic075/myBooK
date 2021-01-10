from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LogowanieForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RejestracjaUzytkownika(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='AgainPassword', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Niestety hasła nie są takie same!!")
        return cd['password2']


class FormularzEdycjiUzytkownika(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class FormularzEdycjiProfilu(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('city', 'date_of_birth','phoneNumber ', 'photo')

