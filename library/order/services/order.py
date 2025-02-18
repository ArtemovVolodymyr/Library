from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from authentication.enums.role import RoleEnum
from order.models import Order
from order.selectors.order import get_order_by_id_or_none
from utils.time import datetime_now


def validate_data(*, user, created_at, end_at, plated_end_at):
    errors = {}

    if user.role != RoleEnum.VISITOR:
        errors['user'] = ValidationError(
            _('The user is not a visitor!.')
        )

    created_at = created_at if created_at else datetime_now()

    if created_at > plated_end_at:
        errors['plated_end_at'] = ValidationError(
            _('Invalid value.')
        )
    if end_at and created_at > end_at:
        errors['end_at'] = ValidationError(
            _('Invalid value.')
        )

    if errors:
        raise ValidationError(errors)


def validate_instance(instance):
    validate_data(
        user=instance.user,
        created_at=instance.created_at,
        end_at=instance.end_at,
        plated_end_at=instance.plated_end_at
    )


def order_save(instance):
    validate_instance(instance)

    instance.full_clean()
    instance.save()


def order_create(
        *,
        user,
        book,
        plated_end_at
):
    instance = Order(
        user=user,
        book=book,
        plated_end_at=plated_end_at
    )

    order_save(instance)

    return instance


def order_update(
        *,
        instance,
        book,
        user,
        end_at,
        plated_end_at
):
    instance.book = book
    instance.user = user
    instance.end_at = end_at
    instance.plated_end_at = plated_end_at

    order_save(instance)

    return instance


def order_close_by_id(order_id):
    result = False

    if instance := get_order_by_id_or_none(order_id):
        instance.end_at = datetime_now()
        order_save(instance)
        result = True

    return result

def order_create(user, book, plated_end_at):
    new_order = Order(user=user, book=book, plated_end_at=plated_end_at)
    new_order.save()
    return new_order