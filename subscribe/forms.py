from django import forms
from subscribe.models import Subscriber
from django.utils.translation import gettext_lazy as _


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'

        labels={
            'first_name':_('Enter your first name: '),
            'last_name':_('Enter your last name: '),
            'email':_('Enter your email: ')
        }

        error_messages={
            'first_name':{
                'required':_('First name is required')
            },
            'last_name':{
                'required':_('Last name is required')
            },
            'email':{
                'required':_('Email is required')
            },
        }