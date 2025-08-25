from django import template

register = template.Library()

@register.filter(name='split')
def split(value, key):
    return [item.strip() for item in value.split(key)]