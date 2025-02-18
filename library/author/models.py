from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Author(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128, default='')  
    books = models.ManyToManyField('book.Book', related_name='authors_written_by', blank=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_next_free_id(cls):
        existing_ids = set(cls.objects.values_list('id', flat=True))
        if not existing_ids:
            return 1
        return min(set(range(1, max(existing_ids) + 2)) - existing_ids)

    @classmethod
    def get_by_id(cls, author_id):
        try:
            return cls.objects.get(pk=author_id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def delete_by_id(cls, author_id):
        try:
            author = cls.objects.get(pk=author_id)
            author.delete()
            return True
        except cls.DoesNotExist:
            return False

    @classmethod
    def create(cls, name, surname=None):
        # Use default values if not provided
        surname = surname or 'Unknown'

        if name and len(name) <= 20:
            author = cls(name=name, surname=surname)
            author.save()
            return author

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
        }

    def update(self, name=None, surname=None):
        if name and len(name) <= 20:
            self.name = name
        if surname:
            self.surname = surname
        self.save()

    @staticmethod
    def get_all():
        return Author.objects.all()

@receiver(pre_save, sender=Author)
def author_pre_save(sender, instance, **kwargs):
    if not instance.id:
        instance.id = Author.get_next_free_id()
