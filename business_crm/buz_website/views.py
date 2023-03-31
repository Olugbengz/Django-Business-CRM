from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


def home(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.add_message(request, messages.INFO, "You have been logged in!")
			return redirect('home')
		else:
			messages.success(request, "You need to login!")
			return redirect('home')
	else:
		return render(request, 'home.html', {})



def logout_user(request):
	logout(request)
	messages.success("You have been logged out, thank you.")
	return redirect('home')


def register_user(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()

			# For authentication and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.add_message(request, messages.INFO, 'You have been successfully Registered!')
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

