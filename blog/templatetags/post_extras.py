from django import template

register = template.Library()

@register.filter
def next(posts_list, current_index):
    """
    Returns the next element of the list using the current index if it exists.
    Otherwise returns a string containing Nothing After.
    """
    try:
        return posts_list[int(current_index) + 1]  # access the next element
    except:
        return 'Nothing After'  # return empty string in case of exception

@register.filter
def previous(posts_list, current_index):
    """
    Returns the previous element of the list using the current index if it exists.
    Otherwise returns a string containing Nothing Before    .
    """
    try:
        return posts_list[int(current_index) - 1]  # access the previous element
    except:
        return 'Nothing Before'  # return empty string in case of exception


@register.filter
def last_element(posts_list):
        """
        Returns the last element of the list
        Otherwise returns a string containing Failed.
        """
        try:
            return posts_list[len(posts_list) - 1]  # access the previous element
        except:
            return 'Failed'  # return empty string in case of exception

