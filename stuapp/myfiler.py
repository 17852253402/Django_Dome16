from django.template import Library

register = Library()
import markdown

@register.filter
def md(value):
    return markdown.markdown(value)