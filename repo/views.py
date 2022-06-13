from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, UserForm,ReviewForm, ProfileForm,ProjectForm
from .models import User,Projects
from .serializers import ProjectsSerializer,UserSerializer
from rest_framework import generics,permissions
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.reverse import reverse 
from django.contrib.auth.decorators import login_required

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
	projects = Projects.objects.all()	
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
	context={"user":request.user, "user_form":user_form, "profile_form":profile_form ,'projects': projects})

class ProjectsList(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer): 
        serializer.save(owner=self.request.user)

class ProjectsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # new

class UserList(generics.ListAPIView): 
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView): 
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'projects': reverse('project-list', request=request, format=format)
    })

@login_required(login_url='/login/')
def new_project(request):
	if request.method == 'POST':
			form = ProjectForm(request.POST,request.FILES)
			if form.is_valid():
				new_post = form.save()
				new_post.save_repo()
			return redirect('welcome')
	else:
		form = ProjectForm()
	return render(request, 'new_repo.html', {'form': form})

@login_required(login_url='/login/')
def new_review(request):
	if request.method == 'POST':
			form = ReviewForm(request.POST,request.FILES)
			if form.is_valid():
				new_rev = form.save()
				new_rev.save_review()
			return redirect('welcome')
	else:
		form = ReviewForm()
	return render(request, 'new_review.html', {'review_form': form})
def reviews(request):
	