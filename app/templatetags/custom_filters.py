# custom_filters.py

from django import template

register = template.Library()

@register.filter
def add_css_class(field, css):
    return field.as_widget(attrs={'class': css})
