from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def services(request):
  template = loader.get_template('services.html')
  return HttpResponse(template.render())

def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())

def clients(request):
  template = loader.get_template('clients.html')
  return HttpResponse(template.render())

def gallery(request):
  template = loader.get_template('gallery.html')
  return HttpResponse(template.render())

def cleaning(request):
  template = loader.get_template('cleaning.html')
  return HttpResponse(template.render())