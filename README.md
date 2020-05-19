# django-vuejs

## Example

Add the `django_vuejs` application to `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
  ...
  'django_vuejs',
  ...
)
```

In a ModelAdmin

```python
from django_vuejs.mixins import VueJS_25_Mixin as VueJSMixin

@admin.register(Example)
class ExampleAdmin(VueJSMixin, admin.ModelAdmin):
    pass

```

In a template
```
{% load django_vuejs %}

{% block extrahead %}
{{ block.super }}
{% vuejs_js %}
{% endblock %}

```

## Check code in development

```
pipenv shell
pipenv install -r requirements-devel.txt
. scripts/pre-commit.sh
```

## Authors

[<img src="http://www.microdisseny.com/images/web/microdisseny-logo-small.png" width="226">](http://www.microdisseny.com/)

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
