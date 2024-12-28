from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingizni kiriting'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Emailingizni kiriting'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqamingiz (ixtiyoriy)'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Savolingizni yozing', 'rows': 5}),
        }
