#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Fedor Marchenko"
__email__ = "mfs90@mail.ru"
__date__ = "Apr 02, 2015"

from django.conf import settings

SETLINKS_PASSWORD = getattr(settings, 'SETLINKS_PASSWORD', '')
SETLINKS_ENCODING = getattr(settings, 'SETLINKS_ENCODING', "UTF-8")  # Необходимая вам кодировка. (WINDOWS-1251, UTF-8, KOI8-R)
SETLINKS_SERVER = getattr(settings, 'SETLINKS_SERVER', "http://show.setlinks.ru")  # сервер с которого берутся коды ссылок
SETLINKS_CACHENAME = getattr(settings, 'SETLINKS_CACHENAME', lambda x: 'setlinks_{0}'.format(x))
SETLINKS_CACHETIMEOUT = getattr(settings, 'SETLINKS_CACHETIMEOUT', 24*60*60)  # Время обновления кеша в секундах
SETLINKS_SOCKETTIMEOUT = getattr(settings, 'SETLINKS_SOCKETTIMEOUT', 10)  # Ожидание кода, секунд
