from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from . import forms
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.urls import reverse_lazy



# Create your views here.
class CustomerSignupView(CreateView):
    model = User
    form_class = forms.CustomerSignupForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("/")

    def form_valid(self, form):
        print("------------------yes valid-----------------")
        user = form.save()
        # Do login
        # username = form.cleaned_data.get('username')
        # password = form.cleaned_data.get('password1')
        # user = authenticate(self.request, username=username, password=password)
        # login(self.request, user)
        

class StaffSignupView(CreateView):
    model = User
    form_class = forms.StaffSignupForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("/")
    

    def form_valid(self, form):
        print("------------------yes valid-----------------")
        user = form.save()
        # Do login
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)

