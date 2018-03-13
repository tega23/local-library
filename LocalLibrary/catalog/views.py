from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin
# Create your views here.



def index(request):
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()

    """Managing user sessions"""
    num_authors=Author.objects.count()
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    

    return render(
        request,
        'catalog/index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors ,'num_authors':num_authors,'num_visits':num_visits},
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

class LoanedBooksByUserListView(generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = BookInstance
    context_object_name = 'bookinstance_list'
    template_name = 'catalog/user_borrowed_books.html'
    paginate_by = 5
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class BorrowedBooksListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'catalog.can_mark_returned'
    paginate_by = 5
    model = BookInstance
    template_name = 'catalog/borrowed_books_list.html'
    context_object_name = 'borrowed_books'

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact = 'o').order_by('due_back')

        
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
         context ={'author': author_id, 'books_by_author':books_by_author,}
     )
