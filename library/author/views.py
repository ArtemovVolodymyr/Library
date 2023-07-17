from django.urls import reverse

from .forms import AuthorForm
from django.http import JsonResponse
from .models import Author
from django.shortcuts import render, get_object_or_404, redirect


def index_author(request):
    authors = Author.objects.all()
    return render(request, 'index_author.html', {'authors': authors})


def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, "author_detail.html", {"author": author})


def create_author(request):
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        patronymic = request.POST.get("patronymic")

        author = Author.create(name, surname, patronymic)
        if author:
            return redirect(reverse('index_author'))

    return render(request, "create_author.html")

# def create_author(request):
#     form = AuthorForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('index_author')
#     return render(request, 'create_author.html', {'form': form})
def delete_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    author.delete()
    return redirect('index_author')


def update_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)

    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        patronymic = request.POST.get("patronymic")

        author.update(name=name, surname=surname, patronymic=patronymic)
        return JsonResponse({"success": True})

    return render(request, "update_author.html", {"author": author})
