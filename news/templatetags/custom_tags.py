from datetime import datetime
from django import template

register = template.Library()


@register.simple_tag()
def current_time(format_string='%b %d %Y'):
    return datetime.utcnow().strftime(format_string)


@register.simple_tag()
def news_length(news=[]):
    return len(news)


@register.simple_tag()
def post_type(eng_type):
    # топорно вставим типы статей из модели POST - не будем заморачиваться импортом
    types = {'ART': 'Статья',
             'NEWS': 'Новость',
             }
    if eng_type in types:
        return types[eng_type]
    else:
        return ''
