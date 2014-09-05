from django.shortcuts import render

from django.views.generic import TemplateView

class BaseTest(TemplateView):
	template_name="index.html"