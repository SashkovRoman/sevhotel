from django import template
from django.template import Context, Template

register = template.Library()


@register.filter(name='childs_first')
def childs_first(childs, parent):
    if parent: return childs.filter(**{str(parent.__class__.__name__).lower(): parent}).first or None
    return childs.first or None


@register.filter(name='childs_get')
def childs_get(childs, parent):
    if parent: return childs.filter(**{str(parent.__class__.__name__).lower(): parent})
    return childs


@register.filter(name='childs_count')
def childs_count(childs, parent):
    if parent: return len(childs.filter(**{str(parent.__class__.__name__).lower(): parent}))
    return len(childs)


@register.filter(name='append_string')
def append_string(value, arg):
    return "%s%s" % (str(value), str(arg))


@register.simple_tag
def render_context(template, context_key, context, **kwargs):
    return Template(template).render(Context({context_key: context}))


@register.simple_tag
def replace(s, **kwargs):
    if s is None:
        return None

    args = [x.strip() for x in s.split(';')]

    if len(args) < 2:
        return None

    s = args.pop(0)

    for arg in args:
        if arg in kwargs:
            s = str.replace(s, arg, str(kwargs.get(arg)))

    return s
