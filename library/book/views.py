from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .forms import BookForm
from .models import Book


def index_book(request):
    books = Book.objects.all()
    return render(request, 'book/index_book.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book/book_detail.html', {'book': book})


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return JsonResponse({"success": True, "book_id": book.id})
        else:
            return JsonResponse({"success": False, "error": "Invalid book data."})
    else:
        form = BookForm()

    return render(request, "book/create_book.html", {"form": form})


def delete_book(request, book_id):
    success = Book.delete_by_id(book_id)
    return JsonResponse({"success": success})


def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        count = request.POST.get("count")

        book.update(name=name, description=description, count=count)
        return JsonResponse({"success": True})

    return render(request, "update_book.html", {"book": book})
