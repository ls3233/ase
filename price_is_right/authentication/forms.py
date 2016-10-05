from django import forms
from models import User, UserProfile, ParentOrder


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('company',)


class ParentOrderForm(forms.ModelForm):
    class Meta:
        model = ParentOrder
        fields = ('is_sell', 'quantity')


