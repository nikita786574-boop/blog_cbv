from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length = 100,
                               widget=forms.TextInput(
                                   attrs={'class':'form-control mb-1'}
                               ))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control mb-1'}))
    first_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={'class':'form-control mb-1'}))
    last_name = forms.CharField(max_length = 100,
                                widget = forms.TextInput(attrs={'class':'form-control mb-1'}))
    class Meta:
        model = User
        fields = ('username','email','first_name', 'last_name') 
    
    def clean_email(self):
        """
        Проверка Email на уникальность
        """
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(pk = self.instance.pk).exists():
            raise forms.ValidationError('Email адрес должен быть уникальным')
        
        return email
    