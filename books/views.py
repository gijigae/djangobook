from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from books.models import Book, Publisher, Author
from django.views.generic import ListView, DetailView
from django.utils import timezone

# def search_form(request):
#     return render(request, 'search_form.html')


class PublisherList(ListView):
    model = Publisher
    template_name = 'publisher_list.html'
    context_object_name = 'publishers'


class PublisherDetail(DetailView):
    model = Publisher
    template_name = 'publisher_detail.html'
    context_object_name = 'publisher'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context


class PublisherBookList(ListView):
    template_name = 'books_by_publisher.html'
    context_object_name = 'books_by_publisher'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherBookList, self).get_context_data(**kwargs)
        # Add the publisher
        context['publisher'] = self.publisher
        return context


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books': books, 'query': q})

    return render(request, 'search_form.html', {'errors': errors})


def books_for_author(request):
    return render(request, 'book_snippet.html')


class AuthorDetailView(DetailView):
    queryset = Author.objects.all()
    template_name = 'author_detail.html'
    # context_object_name = 'author_list'

    def get_object(self):
        # Call the superclass
        object = super(AuthorDetailView, self).get_object()
        # Record the last accessed date
        object.last_accessed = timezone.now()
        object.save()
        # Return the object
        return object

    # def get_queryset(self):
    #     self.author = get_object_or_404(Author, id=self.args[0])
    #     return Author.objects.filter(author=self.author)

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context['author_list'] = Author.objects.all()
        return context





