from django.db import models
from django.utils.translation import gettext_lazy as _


class RoleEnum(models.IntegerChoices):
    VISITOR = 0, _('Visitor')
    LIBRARIAN = 1, _('Librarian')
