from django import forms
from django.conf import settings


class VueJS_25_Mixin(object):
    @property
    def media(self):
        js = 'js/vue-2.5.17%s.js' % ('' if not settings.DEBUG else '.min')
        return super().media + forms.Media(js=[js])
