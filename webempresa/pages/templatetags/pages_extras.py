from django import template
from pages.models import Page

# registrar en la libreria de templates
register = template.Library()

@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages

