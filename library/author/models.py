from django.db import models



class Author(models.Model):
    name = models.CharField(blank=True, max_length=20)
    surname = models.CharField(blank=True, max_length=20)
    patronymic = models.CharField(blank=True, max_length=20)
    books = models.ManyToManyField('book.Book', related_name='authors')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'{self.name} {self.surname} {self.patronymic}'

    def __repr__(self):
        return f"Author(id={self.pk})"

    @staticmethod
    def get_by_id(author_id):
        """
        :param author_id: SERIAL: the id of an Author to be found in the DB
        :return: author object or None if a user with such ID does not exist
        """
        try:
            return Author.objects.get(pk=author_id)
        except Author.DoesNotExist:
            return None

    @staticmethod
    def delete_by_id(author_id):
        """
        :param author_id: an id of an author to be deleted
        :type author_id: int
        :return: True if the object existed in the DB and was removed or False if it didn't exist
        """
        try:
            author = Author.objects.get(pk=author_id)
            author.delete()
            return True
        except Author.DoesNotExist:
            return False

    @staticmethod
    def create(name, surname, patronymic):
        """
        param name: Describes the name of the author
        type name: str max_length=20
        param surname: Describes the surname of the author
        type surname: str max_length=20
        param patronymic: Describes the patronymic of the author
        type patronymic: str max_length=20
        :return: a new author object which is also written into the DB
        """
        if name and len(name) <= 20 and surname and len(surname) <= 20 and patronymic and len(patronymic) <= 20:
            author = Author(name=name, surname=surname, patronymic=patronymic)
            author.save()
            return author

    def to_dict(self):
        """
        :return: author id, author name, author surname, author patronymic
        :Example:
        | {
        |   'id': 8,
        |   'name': 'fn',
        |   'surname': 'mn',
        |   'patronymic': 'ln',
        | }
        """
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'patronymic': self.patronymic,
        }

    def update(self, name=None, surname=None, patronymic=None):
        """
        Updates the author in the database with the specified parameters.\n
        param name: Describes the name of the author
        type name: str max_length=20
        param surname: Describes the surname of the author
        type surname: str max_length=20
        param patronymic: Describes the patronymic of the author
        type patronymic: str max_length=20
        :return: None
        """
        if name and len(name) <= 20:
            self.name = name
        if surname and len(surname) <= 20:
            self.surname = surname
        if patronymic and len(patronymic) <= 20:
            self.patronymic = patronymic
        self.save()

    @staticmethod
    def get_all():
        """
        Returns data for a JSON request with a QuerySet of all authors.
        """
        return Author.objects.all()
