from django import template

register = template.Library()


def submit_row(context):
    """
    Displays the row of buttons for delete and save.
    """
    opts = context.get('opts', False)
    change = context.get('change', False)
    is_popup = context.get('is_popup', False)
    save_as = context.get('save_as', False)
    return {
        'onclick_attrib': (opts.get_ordered_objects() and change
                           and 'onclick="submitOrderForm();"' or ''),
        'show_delete_link': (not is_popup and context.get('has_delete_permission', False)
                             and (change or context.get('show_delete', False))),
        'show_save_as_new': not is_popup and change and save_as,
        'show_save_and_add_another': context.get('has_add_permission', False) and
                                     not is_popup and (not save_as or context.get('add', False)),
        'show_save_and_continue': not is_popup and context.get('has_change_permission', False),
        'is_popup': is_popup,
        'show_save': True,
    }
submit_row = register.inclusion_tag('nexus/admin/submit_line.html', takes_context=True)(submit_row)
