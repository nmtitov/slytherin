from django import template

register = template.Library()

@register.filter
def equals(value, arg):
    return value == arg

@register.filter
def starts(value, arg):
    return arg.startswith(value)
