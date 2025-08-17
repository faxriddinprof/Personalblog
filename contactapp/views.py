from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
# Create your views here.

def SendMessage(request):
    contact_form = ContactForm()
    template_name='contactapp/contact.html'
    context = {'contact_form':contact_form}
    return render(request, template_name=template_name, context=context)