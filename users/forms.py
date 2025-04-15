from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="", 
        widget=forms.EmailInput(attrs={
            'class': 'input-tab', 
            'placeholder': 'Enter your Email...'
        })
    )
    name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'input-tab', 
            'placeholder': 'Enter your Name'
        })
    )
 

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'input-tab',
            'placeholder': 'Enter a Username'
        })
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''

        self.fields['password1'].widget.attrs.update({
            'class': 'input-tab',
            'placeholder': 'Password...'
        })
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password must be at least 8 characters.</li><li>It must not be too common or entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs.update({
            'class': 'input-tab',
            'placeholder': 'Confirm password'
        })
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Re-enter the same password.</small></span>'

