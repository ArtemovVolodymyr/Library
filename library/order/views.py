from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from authentication.selectors.user import all_visitors, get_user_by_id_or_none
from book.selectors.book import all_books, get_book_by_id_or_none
from order.selectors.order import all_orders, get_order_by_id_or_none, visitor_orders
from order.services.order import order_close_by_id, order_create
from utils.errors import messages_to_html_alert, message_to_html_alert
from utils.time import str_to_datetime


def librarian_orders_view(request):
    context = {'orders': all_orders()}
    return render(request, 'order/librarian_orders.html', context)


def visitor_orders_view(request):
    context = {'orders': visitor_orders(request.user)}
    return render(request, 'order/visitor_orders.html', context)


def order_view(request, order_id):
    if request.method == 'GET':
        context = {'order': get_order_by_id_or_none(order_id)}
        return render(request, 'order/order.html', context)


def order_close(request, order_id):
    if request.method == 'GET':
        order_close_by_id(order_id)
        return redirect(f'/librarian/orders/{order_id}/')


def order_create_view(request):
    context = {
        'visitors': all_visitors(),
        'books': all_books()
    }
    if request.method == 'POST':
        visitor_id = int(request.POST['visitor'])
        book_id = int(request.POST['book'])
        plated_end_at = str_to_datetime(request.POST['plated_end_at'])

        user = get_user_by_id_or_none(visitor_id)
        book = get_book_by_id_or_none(book_id)

        try:
            order_create(
                user=user,
                book=book,
                plated_end_at=plated_end_at
            )
        except ValidationError as errors:
            context['alerts'] = messages_to_html_alert(errors, 'danger')
        else:
            context['alerts'] = message_to_html_alert('You have successfully created the order!', 'success')

    return render(request, 'order/create_order.html', context)
