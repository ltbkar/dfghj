import datetime
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views import generic
from . import models, forms
from .models import Book


class CreateBookView(generic.CreateView):
    template_name = 'books/create_book.html'
    form_class = forms.BookForm
    success_url = '/books/'

    def get_object(self,**kwargs):
        books_id = self.kwargs.get('id')
        return get_object_or_404(Book, id=books_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBookView, self).form_valid(form=form)


# def create_book_view(request):
#     if request.method == 'POST':
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h3>Your book has been created</h3>')
#     else:
#         form = forms.BookForm()
#     return render(request, template_name='books/create_book.html',
#                   context={'form': form})


class BookView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'books'
    model = Book

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')

# def book_view(request):
#     if request.method == 'GET':
#         books = Book.objects.filter().order_by('-id')
#         return render(request, template_name='book.html', context={'books': books})


class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book'

    def get_queryset(self, **kwargs):
        books_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=books_id)

# def book_detail_view(request):
#     if request.method == 'GET':
#         book_id = get_object_or_404(Book, id=id)
#         return render(request, template_name='book_detail.html', context={'book_id': book_id})


def about_views(request):
    if request.method == 'GET':
        return HttpResponse("I am Kanbolot Abibillaev. I am 20 yrs")


def hobbies_views(request):
    if request.method == 'GET':
        return HttpResponse('My hobby is reading books and horse riding')


def current_time_views(request):
    if request.method == 'GET':
        return HttpResponse(datetime.datetime.now().strftime('%I:%M:%S %p'))


class BookListView(generic.ListView):
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')


# def book_list(request):
#     if request.method == 'GET':
#         books = Book.objects.filter().order_by('-id')
#         return render(request, template_name='books/book_list.html',
#                       context={'books': books})


class BookDetail(generic.DetailView):
    template_name = 'books/book_detail.html'
    context_object_name = 'book_id'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')

# def book_detail(request):
#     if request.method == 'GET':
#         book_id = get_object_or_404(models.Book, id=id)
#         return render(request, template_name='books/book_detail.html',
#                       context={'book_id': book_id})
#
#
def create_book(request):
    return None


