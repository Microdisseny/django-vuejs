from django import template
from django_vuejs import JS_VUEJS_25, JS_VUEJS_26

register = template.Library()


@register.inclusion_tag('django_vuejs/tags/vuejs_js.html', takes_context=True)
def vuejs_js_25(context):
    return {
        'js_file': JS_VUEJS_25
    }


@register.inclusion_tag('django_vuejs/tags/vuejs_js.html', takes_context=True)
def vuejs_js_26(context):
    return {
        'js_file': JS_VUEJS_26
    }


@register.inclusion_tag('django_vuejs/tags/vuejs_js.html', takes_context=True)
def vuejs_js(context):
    return vuejs_js_26(context)
