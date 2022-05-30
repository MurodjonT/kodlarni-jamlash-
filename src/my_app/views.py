from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
	template_name = 'index.html'


class AboutPageView(TemplateView):
	template_name = 'about.html'

class FruitsPageView(TemplateView):
	template_name = 'fruits.html'

class SFoodPageView(TemplateView):
	template_name = 'seafood.html'

class ContactPageView(TemplateView):
	template_name = 'contact.html'


# Create your views here.
