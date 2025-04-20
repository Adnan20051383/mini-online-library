from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from author.models import Author


class AuthorListView(ListView):
    model = Author
    template_name = 'author/author_list.html'
    context_object_name = 'authors'


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author/author_form.html'
    fields = ['first_name', 'last_name', 'age', 'id_num']
    success_url = reverse_lazy('author_list')


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'author/author_form.html'
    fields = ['first_name', 'last_name', 'age', 'id_num']
    success_url = reverse_lazy('author_list')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author/author_confirm_delete.html'
    success_url = reverse_lazy('author_list')


class AuthorSearchView(ListView):
    model = Author
    template_name = 'author/author_search.html'
    context_object_name = 'authors'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return Author.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(id_num__icontains=query)
        )