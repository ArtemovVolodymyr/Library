def message_to_html_alert(message, alert_type):
    if type(alert_type) == tuple:
        result = f'<div class="alert alert-{alert_type}" role="alert">{message[0]}: {message[1]}</div>'
    elif type(alert_type) == str:
        result = f'<div class="alert alert-{alert_type}" role="alert">{message}</div>'
    else:
        result = 'error'

    return result


def messages_to_html_alert(messages, alert_type):
    result = ''
    for message in messages:
        result += message_to_html_alert(message, alert_type)
    return result
