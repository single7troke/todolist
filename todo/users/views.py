from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account for  {username}  successfully created!')
			return redirect('Home')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})
