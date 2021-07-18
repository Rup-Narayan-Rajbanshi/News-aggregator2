from django.shortcuts import render
from django.urls import reverse
from .models import Message

from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class ContactView(SuccessMessageMixin,CreateView):
    model = Message
    fields = ('__all__')
    template_name = 'contact.html'
    success_message = "Message Sent successfully"

    def get_success_url(self):
        return reverse('portfolio:contact')
