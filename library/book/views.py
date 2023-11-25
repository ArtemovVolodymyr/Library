from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Book
from .forms import BookForm
from author.models import Author


def index_book(request):
    books = Book.objects.all()
    return render(request, 'book/index_book.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    authors = book.authors.all()  
    return render(request, 'book/book_detail.html', {'book': book, 'authors': authors})
    
def create_book(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        count = request.POST.get("count")
        author_ids = request.POST.getlist("authors")  # предполагается, что у вас есть поле в форме с именем "authors"

        book = Book.create(name, description, count)
        if book:
            authors = Author.objects.filter(id__in=author_ids)
            book.add_authors(authors)
            return redirect(reverse('index_book'))

    authors = Author.objects.all()
    return render(request, "book/create_book.html", {'authors': authors})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('index_book')

def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        count = request.POST.get("count")
        author_ids = request.POST.getlist("authors")  # предполагается, что у вас есть поле в форме с именем "authors"

        book.update(name=name, description=description, count=count)
        authors = Author.objects.filter(id__in=author_ids)
        book.remove_authors(book.authors.all())
        book.add_authors(authors)
        return JsonResponse({"success": True})

    authors = Author.objects.all()
    return render(request, "book/update_book.html", {"book": book, 'authors': authors})
