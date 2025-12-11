from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-created_at')
    return render(request, 'tasks/index.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # ensure new tasks default to Pending via model
            form.save()
            messages.success(request, 'Task added successfully!')
            return redirect('tasks:index')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_edit.html', {'form': form, 'task': None})


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('tasks:index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/add_edit.html', {'form': form, 'task': task})


def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    # toggle status
    task.status = 'Completed' if task.status != 'Completed' else 'Pending'
    task.save()
    messages.success(request, 'Task status updated!')
    return redirect('tasks:index')


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    messages.success(request, 'Task deleted!')
    return redirect('tasks:index')
