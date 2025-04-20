from django.urls import path

from book.views import BookListView, BookCreateView, BookUpdateView, BookDeleteView, BookSearchView

urlpatterns = [
    path('author-book-list/<int:pk>', BookListView.as_view(), name='book_list'),
    path('author-book-search/<str:pk>', BookSearchView.as_view(), name='book_search'),
    path('book-', BookCreateView.as_view(), name='book_create'),
    path('book-edit/<str:pk>', BookUpdateView.as_view(), name='book_update'),
    path('book-delete/<str:pk>', BookDeleteView.as_view(), name='book_delete')
]
