from django.contrib import admin
from django.urls import path
from .views import ContactView

from django.views.generic import TemplateView

app_name = 'portfolio'

urlpatterns = [
    path('', ContactView.as_view(),name='contact'),

]