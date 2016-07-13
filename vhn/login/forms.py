import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(forms.Form):

    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))


    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data


class NewProjectForm(forms.Form):

    project_code = forms.CharField(label='Project Code', max_length=100)
    project_inc = forms.CharField(label='Increment', max_length=100)
    project_name = forms.CharField(label='Project Name', max_length=100)
    project_start = forms.CharField(label='Start Date', max_length=100)
    project_end = forms.CharField(label='Deadline', max_length=100)

    creator_id = forms.CharField(label='creator_id', max_length=100)
    assigned_user_id = forms.CharField(label='assigned_user_id', max_length=500)
    location = forms.CharField(label='location', max_length=1000)
    signedoff = forms.BooleanField(label='signedoff')
    flagdelete = forms.BooleanField(label='flagdelete')
