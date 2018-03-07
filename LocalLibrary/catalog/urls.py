from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name = 'index'),
    path('books/<int:pk>', views.book_detail_view, name = 'book-detail'),
    path('books/', views.BookListView.as_view() , name = 'books'),
    path('authors/<int:pk>', views.author_detail_view , name = 'author-detail'), 
    #path('catalog/author/<int :id>', views. , name = ''),
]

