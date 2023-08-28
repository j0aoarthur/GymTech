from django import template
from datetime import datetime, date

register = template.Library()

@register.filter(expects_localtime=True)
def is_past(value):
    if isinstance(value, datetime):
        value = value.date()
    return value < date.today()

@register.filter
def starts_with(value, prefix):
    return value.startswith(prefix)