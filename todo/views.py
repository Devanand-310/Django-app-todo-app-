from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    if todos is None:
        todos = []
    return render(request,'todo/index.html',{'todos':todos})

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
    return render(request, 'todo/add_todo.html',{'form':form})

def update_todo(request, pk):
    todo =Todo.objects.get(pk=pk)     
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/update_todo.html', {'form': form})

def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('index')
    return render(request, 'todo/delete_todo.html', {'todo': todo})

def complete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = True
    todo.save()
    return redirect('index')