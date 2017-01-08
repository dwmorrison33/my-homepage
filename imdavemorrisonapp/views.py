from django.shortcuts import render, redirect
from imdavemorrisonapp.forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
import re

def home(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form.save()
		#Need to add send_mail function here
		messages.success(request, "Your message was sent, I will be in contact with you soon!")
		return redirect('home')
	return render(request, 'home.html', {'form': form,})