from authentication.enums.role import RoleEnum
from authentication.models import CustomUser
from utils.choise import get_choice_label
from utils.time import datetime_to_timestamp


def all_users():
    return CustomUser.objects.all()


def all_visitors():
    return CustomUser.objects.filter(role=RoleEnum.VISITOR)


def get_user_by_id_or_none(user_id):
    return CustomUser.objects.filter(id=user_id).first()


def get_user_by_email_or_none(email):
    return CustomUser.objects.filter(email=email).first()


def user_to_dict(instance):
    return {
        'id': instance.id,
        'first_name': instance.first_name,
        'middle_name': instance.middle_name,
        'last_name': instance.last_name,
        'email': instance.email,
        'created_at': datetime_to_timestamp(instance.created_at),
        'updated_at': datetime_to_timestamp(instance.updated_at),
        'role': instance.role,
        'is_active': instance.is_active
    }


def user_to_str(instance):
    return f"'id': {instance.id}, " \
           f"'first_name': '{instance.first_name}', " \
           f"'middle_name': '{instance.middle_name}', " \
           f"'last_name': '{instance.last_name}', " \
           f"'email': '{instance.email}', " \
           f"'created_at': {datetime_to_timestamp(instance.created_at)}, " \
           f"'updated_at': {datetime_to_timestamp(instance.updated_at)}, " \
           f"'role': {instance.role}, " \
           f"'is_active': {instance.is_active}"


def get_user_role_name(instance):
    return get_choice_label(
        choices=RoleEnum.choices,
        value=instance.role
    )
