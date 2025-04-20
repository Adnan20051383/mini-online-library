from django.urls import path

from author import views
from author.views import AuthorListView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView, AuthorSearchView

urlpatterns = [
    path('author-list', AuthorListView.as_view(), name='author_list'),
    path('author-create', AuthorCreateView.as_view(), name='author_create'),
    path('author-update/<str:pk>', AuthorUpdateView.as_view(), name='author_update'),
    path('author-delete/<str:pk>', AuthorDeleteView.as_view(), name='author_delete'),
    path('author-search/', AuthorSearchView.as_view(), name='author_search')
]
