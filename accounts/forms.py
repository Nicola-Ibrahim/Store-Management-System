from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import transaction
from . import models

class CustomerSignupForm(UserCreationForm):
    # interests = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    phone_number = forms.IntegerField()
    state = forms.CharField()
    city = forms.CharField()
    street = forms.CharField()
    zipcode = forms.IntegerField()


    @transaction.atomic
    def save(self, commit: bool = True):
        user = super().save(commit=False)
        user.is_staff = False
        user.is_admin = False
        user.save()
        user.refresh_from_db()
        if commit:
            models.Person.objects.create(
                user=user,
                phone_number=self.cleaned_data.get('phone_number'),      
                state=self.cleaned_data.get('state'),
                city=self.cleaned_data.get('city'),
                street=self.cleaned_data.get('street'),
                zipcode=self.cleaned_data.get('zipcode'),
            )
            
        return user



class StaffSignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    STANDARD = 'STD'
    MANAGER = 'MGR'
    SR_MANAGER = 'SRMGR'
    PRESIDENT = 'PRES'

    EMPLOYEE_TYPES = (
        (STANDARD, 'base employee'),
        (MANAGER, 'manager'),
        (SR_MANAGER, 'senior manager'),
        (PRESIDENT, 'president')
    )

    phone_number = forms.IntegerField()
    state = forms.CharField()
    city = forms.CharField()
    street = forms.CharField()
    zipcode = forms.IntegerField()
    role = forms.MultipleChoiceField(choices=EMPLOYEE_TYPES)
    manager_id = forms.IntegerField()


    @transaction.atomic
    def save(self, commit: bool = True):
        user = super().save(commit=False)
        user.is_staff = False
        user.save()
        user.refresh_from_db()
        if commit:
            models.Person.objects.create(
                user=user,
                phone_number=self.cleaned_data.get('phone_number'),      
                state=self.cleaned_data.get('state'),
                city=self.cleaned_data.get('city'),
                street=self.cleaned_data.get('street'),
                zipcode=self.cleaned_data.get('zipcode'),
                role=self.cleaned_data.get('role'),
                manager_id=self.cleaned_data.get('manager_id')
            )
            
            
        return user


