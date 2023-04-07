from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddNewCustomerForm
from .models import Record


def home(request):
	records = Record.objects.all()
	if request.method == "POST":
		username = request.POST['first_name']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user :
			login(request, user)
			messages.success(request, messages.INFO, "You have been logged in!")
			return redirect('home')
		else:
			messages.success(request, "You need to login!")
			return redirect('home')
	else:
		return render(request, 'home.html', {'records': records})



def logout_user(request):
	logout(request)
	messages.success(request, "You have been logged out, thank you.")
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



def customer_details(request, pk):
	if request.user.is_authenticated:
		customer_details = Record.objects.get(id=pk)
		return render(request, 'customer.html', {'customer_details': customer_details})

	else:
		messages.success(request, "You need to login to access this information!")
		return redirect('home')


def delete_record(request, pk):
	if request.user.is_authenticated:
		record_to_delete = Record.objects.get(id=pk)
		record_to_delete.delete()
		messages.success(request, "Record successfully deleted!")
		return redirect('home')
	else:
		messages.success(request, "Only an admin can delete customer's imformation information!")
		return redirect('home')


def add_record(request):
	form = AddNewCustomerForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == 'POST':
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record successfully added!")
				return redirect('home')				
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "Login is required to add customer's record!")
		return redirect('home')



def update_record(request, pk):
	if request.user.is_authenticated:
		this_record = Record.objects.get(id=pk)
		form = AddNewCustomerForm(request.POST or None, instance=this_record)
		if form.is_valid():
			form.save()
			messages.success(request, "This record has been updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "Login is required to add customer's record!")
		return redirect('home')
