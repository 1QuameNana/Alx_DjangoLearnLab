from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import View 
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm
#from .forms import BookForm

from .models import Book, UserProfile
from .models import Library




def list_books(request):
    items = Book.objects.all()
    book_list = [f"{i.title} by {i.author}" for i in items]
    return render(request, "relationship_app/list_books.html", {"book_list": book_list})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['library'] = self.object
        return context