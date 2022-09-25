from django import template

register = template.Library()


@register.filter(name='splt')
def splt(s):
    return s.split(',')
