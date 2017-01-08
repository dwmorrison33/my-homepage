from django import forms

from imdavemorrisonapp.models import Contact

class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact
		fields = ['name', 'user_type', 'email', 'message']
        widgets = {
                'name': forms.TextInput(attrs={'placeholder': 'Name'}),
                'email': forms.EmailInput(attrs={'placeholder': '     Email'}),
                'message': forms.TextInput(attrs={'placeholder': 'Message'}),
                }