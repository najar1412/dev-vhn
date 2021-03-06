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

class UpdateRegistrationForm(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=100, required=False)
    last_name = forms.CharField(label='last_name', max_length=100, required=False)
    cakeday = forms.CharField(label='cakeday', max_length=100, required=False)
    med_provider = forms.CharField(label='med_provider', max_length=100, required=False)
    med_plan = forms.CharField(label='med_plan', max_length=100, required=False)
    dent_provider = forms.CharField(label='dent_provider', max_length=100, required=False)
    dent_plan = forms.CharField(label='dent_plan', max_length=100, required=False)

class ProjectNewForm(forms.Form):
    code = forms.CharField(label='code', max_length=200)
    inc = forms.CharField(label='inc', max_length=10)

class AssetForm(forms.Form):
    collection = forms.CharField(label='collection', max_length=100)
    project_id = forms.CharField(label='project_id', max_length=100, required=False)
    name = forms.CharField(label='name', max_length=100, required=False)
    item = forms.CharField(label='item', max_length=100, required=False)
    item_thumb = forms.CharField(label='item_thumb', max_length=100, required=False)
    tag = forms.CharField(label='tag', max_length=500, required=False)
    member_id = forms.CharField(label='member_id', max_length=1000, required=False)
