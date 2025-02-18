from django.db import models
from author.models import Author


class Book(models.Model):
    name = models.CharField(blank=True, max_length=128)
    description = models.CharField(blank=True, max_length=256)
    count = models.IntegerField(default=10)
    id = models.AutoField(primary_key=True, editable=False)

    authors = models.ManyToManyField(Author, related_name='books_authored')

    def __str__(self):
        return self.name

    def get_authors(self):
        return self.authors.all()

    @classmethod
    def get_next_free_id(cls):
        existing_ids = set(cls.objects.values_list('id', flat=True))
        if not existing_ids:
            return 1
        return min(set(range(1, max(existing_ids) + 2)) - existing_ids)

    @classmethod
    def get_by_id(cls, book_id):
        try:
            return cls.objects.get(pk=book_id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def delete_by_id(cls, book_id):
        try:
            book = cls.objects.get(pk=book_id)
            book.delete()
            return True
        except cls.DoesNotExist:
            return False

    @classmethod
    def create(cls, name, description):
        book = cls()
        book.id = cls.get_next_free_id()
        book.name = name
        book.description = description
        book.save()
        return book

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'count': self.count,
            'authors': [author.name for author in self.authors.all()]  # assuming you have an 'Author' model
        }

    def update(self, name=None, description=None, count=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if count is not None:
            self.count = count
        self.save()

    def add_authors(self, authors):
        if authors is not None:
            for elem in authors:
                self.authors.add(elem)
        self.save()

    def remove_authors(self, authors):
        for elem in authors:
            self.authors.remove(elem)
        self.save()

    @staticmethod
    def get_all():
        return list(Book.objects.all())
