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



class BookListView(generic.ListView):
    model = Book
    
    context_object_name = 'book_list'
    template_name = 'book_list.html'
    """py
    def get_queryset(self):
        return Book.objects.filter(title__icontains = 'war' )[:5]
    """
    def get_context_data(self , **kwargs):
        context = super(BookListView , self).get_context_data(**kwargs)
        context['some_data']= 'This is just some data'
        return context

def book_detail_view(request , pk):
    book_id = Book.objects.get(pk = pk)
    return render(
        request,
        'catalog/book_detail.html',
        context ={'book': book_id}           
    )

def author_detail_view( request , pk):
    pass