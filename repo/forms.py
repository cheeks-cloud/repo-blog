from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Projects

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

		
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
	class Meta: 
		model = Profile
		fields = ('projects',)


class ProjectForm(forms.ModelForm):
	class Meta: 
		model = Projects
		exclude = ['created','owner']
		title = forms.CharField(max_length=40)
		image = forms.ImageField()
		description = forms.CharField()
		link= forms.URLField()