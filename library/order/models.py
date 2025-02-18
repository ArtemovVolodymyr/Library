from django.db import models, IntegrityError
from django.db import transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver

from authentication.models import CustomUser
from book.models import Book


class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    end_at = models.DateTimeField(null=True, blank=True)
    plated_end_at = models.DateTimeField()
    id = models.AutoField(primary_key=True, editable=False)


    def __str__(self):
        return f'{self.book}, {self.user}'

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id})'

    @classmethod
    def get_next_free_id(cls):
        existing_ids = set(cls.objects.values_list('id', flat=True))
        if not existing_ids:
            return 1
        return min(set(range(1, max(existing_ids) + 2)) - existing_ids)


def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    try:
        with transaction.atomic():
            # Check if the book is used in any order
            if Order.objects.filter(book=book).exists():
                # Assign a new book to orders that use the current book
                new_book = Book.objects.exclude(id=book_id).first()
                if new_book:
                    Order.objects.filter(book=book).update(book=new_book)
            book.delete()
    except ProtectedError:
        # Handle protected error, for example, show an error message
        pass

    return redirect('index_book')
