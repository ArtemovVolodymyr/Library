from order.models import Order


def order_to_str(instance):
    def datetime_to_string(datetime):
        return f'\'{datetime}\'' if datetime else None

    dts = datetime_to_string

    return f"'id': {instance.id}, " \
           f"'user': {repr(instance.user)}, " \
           f"'book': {repr(instance.book)}, " \
           f"'created_at': {dts(instance.created_at)}, " \
           f"'end_at': {dts(instance.end_at)}, " \
           f"'plated_end_at': {dts(instance.plated_end_at)}"


def order_to_dict(instance):
    return {
        'id': instance.id,
        'book': instance.book.id,
        'user': instance.user.id,
        'created_at': instance.created_at,
        'end_at': instance.end_at,
        'plated_end_at': instance.plated_end_at,
    }


def get_order_by_id_or_none(order_id):
    return Order.objects.filter(id=order_id).first()


def all_orders():
    return Order.objects.all()


def visitor_orders(visitor):
    return Order.objects.filter(user=visitor)


def get_not_returned_books():
    return Order.objects.filter(end_at=None)
