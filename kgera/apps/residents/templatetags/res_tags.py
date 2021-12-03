from django import template
from ..models import Houses

register = template.Library()


@register.filter(name='get_id', is_safe=True)
def get_id(house_code):
    house_id = Houses.objects.get(housecode=house_code).id

    return house_id
