from django import forms
from django_quill.widgets import QuillWidget

# Create your forms here.

class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50, label='Ad')
	last_name = forms.CharField(max_length = 50, label='Soyad')
	email_address = forms.EmailField(max_length = 150, label='Email')
	message = forms.CharField(widget = forms.Textarea, max_length = 2000,label="Mesaj")


	first_name.widget.attrs.update({'class': 'contact-input'})
	last_name.widget.attrs.update({'class': 'contact-input'})
	email_address.widget.attrs.update({'class': 'contact-input'})
	message.widget.attrs.update({'class': 'contact-input h-52 outline-none'})


class NewsletterForm(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=forms.Textarea, label="Email content")

    subject.widget.attrs.update({'class': 'contact-input'})
    receivers.widget.attrs.update({'class': 'contact-input'})
    message.widget.attrs.update({'class': 'contact-input h-52 outline-none'})
    
