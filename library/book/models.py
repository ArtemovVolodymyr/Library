from django.db import models

class Book(models.Model):
    name = models.CharField(blank=True, max_length=128)
    description = models.CharField(blank=True, max_length=256)
    count = models.IntegerField(default=10)
    authors = models.ManyToManyField('author.Author', related_name='books')

    def __str__(self):
        return self.name

    def get_authors(self):
        return self.authors.all()

    @staticmethod
    def get_next_free_id():
        existing_ids = set(Book.objects.values_list('id', flat=True))
        if not existing_ids:
            return 1
        max_id = max(existing_ids)
        for i in range(1, max_id + 2):
            if i not in existing_ids:
                return i

    @staticmethod
    def get_by_id(book_id):
        return Book.objects.get(id=book_id) if Book.objects.filter(id=book_id).exists() else None

    @staticmethod
    def delete_by_id(book_id):
        if Book.get_by_id(book_id) is None:
            return False
        Book.objects.get(id=book_id).delete()
        return True

    @staticmethod
    def create(name, description, count=10):
        if len(name) > 128:
            return None

        book = Book()
        book.id = Book.get_next_free_id()
        book.name = name
        book.description = description
        book.count = count
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
