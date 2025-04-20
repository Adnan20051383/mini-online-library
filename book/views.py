from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from author.models import Author
from book.models import Book


class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        author = Author.objects.get(pk=self.kwargs.get('pk', ''))
        return Book.objects.filter(author=author)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Author.objects.get(pk=self.kwargs.get('pk', ''))
        context['author'] = author
        return context

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'year']
    template_name = 'book/book_form.html'

    def get_success_url(self):
            return reverse_lazy('book_list', kwargs={'pk': self.object.author.pk})


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'year']
    template_name = 'book/book_form.html'

    def get_success_url(self):
        return reverse_lazy('book_list', kwargs={'pk': self.object.author.pk})


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book/book_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('book_list', kwargs={'pk': self.object.author.pk})


class BookSearchView(ListView):
    model = Book
    template_name = 'book/book_search.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        author = Author.objects.get(pk=self.kwargs.get('pk', ''))
        return Book.objects.filter(author=author, title__icontains=query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Author.objects.get(pk=self.kwargs.get('pk', ''))
        context['author'] = author
        return context
