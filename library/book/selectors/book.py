from book.models import Book


def all_books():
    return Book.objects.all()


def get_book_by_id_or_none(book_id):
    return Book.objects.filter(id=book_id).first()
