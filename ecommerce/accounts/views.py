from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout, login, authenticate
from .forms import LoginForm, RegistrationForm

def logout_view(request):
	logout(request)

	return redirect(reverse('home'))

def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password = password)
			login(request, user)
			return redirect('home')
	else:
		form = LoginForm()
	context = {'form': form}
	return render(request, 'accounts/login_form.html', context=context)


def registration_view(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
	 		new_user = form.save(commit=False)
	 		new_user.save()
	# 		username = form.cleaned_data['username']
	# 		password = form.cleaned_data['password']
	# 		user = authenticate(username=username, password = password)
	# 		login(request, user)
	# 		return redirect('home')
	else:
		form = RegistrationForm()
	context = {'form': form}
	return render(request, 'accounts/registration_form.html', context=context)
