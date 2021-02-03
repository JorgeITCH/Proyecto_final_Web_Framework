from django import template

from polls.models import Department

register = template.Library()

@register.simple_tag
def departments():
    return Department.objects.all()