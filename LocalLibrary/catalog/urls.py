from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name = 'index'),
    path('books/', views.BookListView.as_view() , name = 'books'),
    path('books/<int:pk>', views.book_detail_view, name = 'book-detail'),
    path('author/', views.AuthorListView.as_view() , name = 'authors'),
    path('authors/<int:pk>', views.author_detail_view , name = 'author-detail'),   
]

