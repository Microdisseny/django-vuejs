from django import forms

from . import JS_VUEJS_25, JS_VUEJS_26


class VueJS_25_Mixin(object):

    @property
    def media(self):
        return super().media + forms.Media(js=[JS_VUEJS_25])


class VueJS_26_Mixin(object):

    @property
    def media(self):
        return super().media + forms.Media(js=[JS_VUEJS_26])


class VueJSMixin(VueJS_26_Mixin):
    pass
