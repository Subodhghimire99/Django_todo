from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import todo
from .forms import todo_form

def todo_view(request,*args,**kwargs):
	todo_form_obj = todo_form()
	todos=todo.objects.all()
	if request.method == 'POST':
		todo_form_obj = todo_form(request.POST)
		if todo_form_obj.is_valid():
			todo.objects.create(**todo_form_obj.cleaned_data)
			todo_form_obj=todo_form()
	context={
		"form":todo_form_obj,
		"t":todos,
	}
	return render(request,"todo/base.html",context)

def delete_view(request,num):
	delete_item = todo.objects.get(id=num)
	print(delete_item)
	return render(request,"todo/base.html",{})