from django import template

register = template.Library()

#Multiplication
@register.filter(name='mul') 
def mul(value, arg):
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return value