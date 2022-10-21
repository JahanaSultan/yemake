from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User

        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            "first_name": "Ad Soyad",
            'username': 'İstifadəçi Adı'
        }

    def __init__(self, *args, **kwargs):
      super(CustomUserCreationForm, self).__init__(*args, **kwargs)
      for name, field in self.fields.items():
         field.widget.attrs.update({'class': 'input-signup'})
      self.fields['first_name'].widget.attrs['placeholder'] = 'Ad Soyad'
      self.fields['email'].widget.attrs['placeholder'] = 'Email'
      self.fields['username'].widget.attrs['placeholder'] = 'İstifadəçi Adı'
      self.fields['password1'].widget.attrs['placeholder'] = 'Şifrə'
      self.fields['password2'].widget.attrs['placeholder'] = 'Təkrar Şifrə'
    

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        email=forms.CharField(error_messages={'unique': u'My custom message'}) 
        fields=["name","cover_image","profile_image","username","short_info"]
        labels = {
            "cover_image": "Örtük Şəkli",
            'profile_image': 'Profil Şəkli',
            "name":"Ad Soyad",
            "username":"İstifadəçi Adı",
            "short_info":"Qısa Məlumat",
        }
       
            
            
       
            