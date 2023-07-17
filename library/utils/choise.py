def get_choice_label(*, choices, value):
    for item in choices:
        if item[0] == value:
            return item[1]
    return ''


def exists_choice_value(*, choices, value):
    for item in choices:
        if item[0] == value:
            return True
    return False
