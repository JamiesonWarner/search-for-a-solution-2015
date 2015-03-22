from django import forms

class ProjectForm(forms.Form):
  title = forms.CharField(label='Project Title')
  description = forms.CharField(widget=forms.Textarea, label='Description')
  owner = forms.CharField(label='Name')
  owner_role = forms.CharField(label='Role')
  owner_email = forms.CharField(label='Email')
  seeking_designer = forms.BooleanField(required=False)
  seeking_developer = forms.BooleanField(required=False)
  seeking_business = forms.BooleanField(required=False)
