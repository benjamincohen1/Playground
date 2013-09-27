from django.template import Template, Context
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from forms import ContactForm
import datetime
from books.models import *
def root(request):
	return HttpResponse("Welcome to the root")
def hello(request):
	return HttpResponse("Hello World!")
def time(request):
    now = datetime.datetime.now()
    return render(request,'date.html',Context({'date':now}))
def dispNum(request,num):
	return HttpResponse(num)
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})
