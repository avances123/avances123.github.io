#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Fabio Rueda'
SITENAME = u'Fabio Rueda'
SITEURL = ''
THEME="pelican-bootstrap3"
PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
            ('Cloudtrum', 'http://www.cloudtrum.xyz'),
        )

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/avances123'),
          ('Google+', 'https://plus.google.com/u/0/+FabioRuedaCarrascosa/posts'),)

DEFAULT_PAGINATION = 10

TWITTER_USERNAME="avances123"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

BOOTSTRAP_THEME = "flatly"
PYGMENTS_STYLE = "monokai"
GITHUB_URL="http://github.com/avances123"
