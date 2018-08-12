from django import template

register = template.Library()

@register.filter
def next(posts_list, current_index):
    """
    Returns the next element of the list using the current index if it exists.
    Otherwise returns an empty string.
    """
    try:
        return posts_list[int(current_index) + 1]  # access the next element
    except:
        return ''  # return empty string in case of exception

@register.filter
def previous(posts_list, current_index):
    """
    Returns the previous element of the list using the current index if it exists.
    Otherwise returns an empty string.
    """
    try:
        return posts_list[int(current_index) - 1]  # access the previous element
    except:
        return ''  # return empty string in case of exception
