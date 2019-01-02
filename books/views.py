from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from utils.forms import DeleteConfirmForm

from .forms import BookForm
from .models import Book

@login_required
def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

@login_required
def show(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/show.html', {'book': book})


def add(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, '新增成功')
        return redirect('books:index')

    return render(request, 'books/add.html', {'form': form})


def edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        messages.success(request, '更新成功')
        return redirect('books:index')

    return render(request, 'books/edit.html', {'form': form})


def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check']:
        book.delete()
        return redirect('books:index')

    return render(request, 'books/delete.html', {'form': form})
