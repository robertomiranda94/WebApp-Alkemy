from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from jinja2 import Environment


def ini_jinja2(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })

    return env
