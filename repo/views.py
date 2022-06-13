from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, UserForm, ProfileForm
from .models import User,Projects

# Create your views here.
def welcome(request):
	projects = Projects.objects.all()	
	return render( request, "projects.html", {'projects': projects})

def register_request(request):

	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('login')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("welcome")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("welcome")


def userpage(request):
	if request.method == "POST":
		user_form = UserForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, instance=request.user.profile)
		if user_form.is_valid():
			user_form.save()
			messages.success(request,('Your profile was successfully updated!'))
		elif profile_form.is_valid():
			profile_form.save()
			messages.success(request,('Your wishlist was successfully updated!'))
		else:
			messages.error(request,('Unable to complete request'))
		return redirect('userpage')
		
	user_form = UserForm(instance=request.user)
	profile_form = ProfileForm(instance=request.user.profile)
	return render(request=request, template_name="profile.html", 
	context={"user":request.user, "user_form":user_form, "profile_form":profile_form })






