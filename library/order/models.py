from django.db import models

from authentication.models import CustomUser
from book.models import Book


class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    end_at = models.DateTimeField(null=True, blank=True)
    plated_end_at = models.DateTimeField()

    def __str__(self):
        return f'{self.book}, {self.user}'

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id})'
