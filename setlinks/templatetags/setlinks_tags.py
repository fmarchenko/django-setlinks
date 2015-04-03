#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Fedor Marchenko"
__email__ = "mfs90@mail.ru"
__date__ = "Apr 02, 2015"

from django import template
from django.core.cache import cache
from .. import settings as conf
from ..utils import Hash
import urllib2

register = template.Library()


@register.inclusion_tag('setlinks/tags/get_links.html', takes_context=True)
def get_links(context):
    _host = context['request'].get_host()
    _path = context['request'].path
    _cache_name = conf.SETLINKS_CACHENAME(_path)
    _url = '{server}/?host={host}&k={encoding}&p={password}'.format(
        server=conf.SETLINKS_SERVER, host=_host,
        encoding=conf.SETLINKS_ENCODING, password=conf.SETLINKS_PASSWORD
    )
    _pageid = Hash.getCRC32('%s%s' % (_host, _path), conf.SETLINKS_ENCODING)
    _links = cache.get(_cache_name)

    if not _links:
        resp = urllib2.urlopen(_url, timeout=conf.SETLINKS_SOCKETTIMEOUT)
        html = resp.read()
        if len(html) > 20:
            info = html[:html.index('\n')].split('\t')
            if conf.SETLINKS_PASSWORD == info[1]:
                server_cache_time = int(info[0])
                page = html[html.index('\n')+1:]
                lines = page.split('\n')
                _links = []
                for line in lines:
                    _links.append(line.split('\t'))
                cache.set(_cache_name, _links, conf.SETLINKS_CACHETIMEOUT)
            else:
                _links = []
        else:
            _links = []

    _page_links = []
    for link in _links:
        if long(link[0] if link[0] != '' else 0) == _pageid:
            _page_links.append(link[1])

    # context['html'] = _links, _pageid

    context['password'] = conf.SETLINKS_PASSWORD
    context['links'] = _page_links
    return context