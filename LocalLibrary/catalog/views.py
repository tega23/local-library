from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.shortcuts import get_object_or_404
# Create your views here.



def index(request):
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()

    return render(
        request,
        'catalog/index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5
    context_name ='author_list'
    tempelate_name = 'author_list.html'

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        return context
class BookListView(generic.ListView):
    model = Book
    paginate_by = 5
    context_object_name = 'book_list'
    template_name = 'book_list.html'
    
    def get_context_data(self , **kwargs):
        context = super(BookListView , self).get_context_data(**kwargs)
        return context

def book_detail_view(request , pk):
    book_id = Book.objects.get(pk = pk)
    return render(
        request,
        'catalog/book_detail.html',
        context ={'book': book_id}           
    )

def author_detail_view(request , pk):
     author_id = Author.objects.get(pk= pk)
     books_by_author = Book.objects.filter(author = author_id)
     return render(
         request,
         'catalog/author_detail.html',
         context ={'author': author_id, 'books_by_author':books_by_author}
     )
