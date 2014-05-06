from random import choice

from markupsafe import Markup
from pyramid.renderers import render


images = [
    'tux',
    'linuxtag',
    'amadeus',
]

texts = [
    'Lorem ipsum...',
    'This could be your custom message!',
    'Hi there!',
]

template = 'oscad_theme_linuxtag:templates/oscad_theme_linuxtag/extra.jinja2'


def lsuc_extra_info(request, lsuc, osuc):
    return Markup(render(template, {
        'image': choice(images),
        'text': choice(texts),
    }, request=request))


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.registry.settings.oscad_settings.lsuc_extra_info = lsuc_extra_info
