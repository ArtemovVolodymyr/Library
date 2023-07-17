from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from authentication.enums.role import RoleEnum
from authentication.models import CustomUser
from authentication.selectors.user import get_user_by_id_or_none
from utils.choise import exists_choice_value


def _validate_fields(instance):
    errors = {}

    if not exists_choice_value(choices=RoleEnum.choices, value=instance.role):
        errors['role'] = ValidationError(
            _('The role is not exists.')
        )

    if errors:
        raise ValidationError(errors)


def user_save(instance):
    _validate_fields(instance)

    instance.full_clean()
    instance.save()


def user_create(
        *,
        email,
        password,
        first_name,
        middle_name,
        last_name,
        role
):
    instance = CustomUser(
        email=email,
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        role=role
    )

    instance.set_password(password)

    user_save(instance)

    return instance


def user_update(
        *,
        instance,
        first_name,
        last_name,
        middle_name,
        password,
        role,
        is_active
):
    instance.first_name = first_name
    instance.last_name = last_name
    instance.middle_name = middle_name
    instance.set_password(password)
    instance.role = role
    instance.is_active = is_active

    user_save(instance)

    return instance


def user_delete(instance):
    instance.delete()


def user_delete_by_id(user_id):
    result = False

    if instance := get_user_by_id_or_none(user_id):
        user_delete(instance)
        result = True

    return result
