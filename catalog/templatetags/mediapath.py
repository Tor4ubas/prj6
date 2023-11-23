from django import template
from django.templatetags.static import static

register = template.Library()

@register.filter
def mediapath(file_path):
    return static(file_path)
