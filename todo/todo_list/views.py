from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ToDo


def home(request):
	if request.user.is_authenticated:
		return redirect('Mylist')
	else:
		text = ['Create', 'Your', 'Own', 'List!']
		return render(request, 'todo_list/home.html', {'text': text})


@login_required
def mylist(request):
	todo_list = ToDo.objects.filter(author=request.user.id)[::-1]
	return render(request, 'todo_list/mylist.html', {'todo_list': todo_list})


@login_required
def add(request):
	try:
		text = request.POST['content']
		if request.method == 'POST' and text:
			new_todo = ToDo.objects.create(content=text, author=request.user)
			new_todo.save()
			return redirect('Mylist')
		else:
			messages.warning(request, "please type something before add")
			return redirect('Mylist')
	except:
		return redirect('Mylist')


@login_required
def done(request, todo_id):
	try:
		ToDo.objects.filter(id=todo_id, author=request.user.id).update(complete=True)
		return redirect('Mylist')
	except:
		return redirect('Mylist')


@login_required
def delete(request, todo_id):
	try:
		ToDo.objects.filter(id=todo_id, author=request.user.id).delete()
		return redirect('Mylist')
	except:
		return redirect('Mylist')
