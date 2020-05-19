from django.conf import settings

JS_VUEJS_25 = 'js/vuejs/vue-2.5.17%s.js' % ('' if not settings.DEBUG else '.min')
JS_VUEJS_26 = 'js/vuejs/vue-2.6.11%s.js' % ('' if not settings.DEBUG else '.min')
