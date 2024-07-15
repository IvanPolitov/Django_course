from django import template

from news.models import Category

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_category(a1=0, a2=1):
    categories = Category.objects.all()
    return {"categories": categories, 'a1': a1, 'a2': a2}
