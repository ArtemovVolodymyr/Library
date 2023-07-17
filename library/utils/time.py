from datetime import datetime

from django.utils import timezone
from django.utils.timezone import make_aware


def datetime_to_timestamp(value):
    return int(value.timestamp())


def datetime_now():
    return timezone.now()


def str_to_datetime(data):
    return make_aware(datetime.strptime(data, '%m/%d/%Y'))
