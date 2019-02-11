from django.shortcuts import render
from .models import todo

from .forms import addtodo_form

def todo_view(request,*args,**kwargs):
	raw_form = addtodo_form()
	all_todo = todo.objects.all()
	if request.method == 'POST' and 'add' in request.POST:
		raw_form_data = addtodo_form(request.POST)
		if raw_form_data.is_valid():
			todo.objects.create(**raw_form_data.cleaned_data)
			raw_form = addtodo_form()
	# if request.method == 'POST' and 'delete' in request.POST:
		# todo.getobject()
	context = {
		"form":raw_form,
		"all":all_todo
	}
	return render(request,"todo/base.html",context)
# def delete_view(request,*args,**kwargs):