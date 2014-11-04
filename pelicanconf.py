#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Fabio Rueda'
SITENAME = u'Mis POCs'
SITEURL = ''
THEME="tema"
PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = u'es'

PLUGIN_PATHS = ["plugins"]
PLUGINS = ['related_posts','sitemap']


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
            ('Cloudtrum', 'http://www.cloudtrum.xyz'),
        )
PROJECTS = (
            ('fa-bitcoin','Cloudtrum', 'http://www.cloudtrum.xyz'),
        )

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/avances123'),
          ('Google+', 'https://plus.google.com/u/0/+FabioRuedaCarrascosa/posts'),)

DEFAULT_PAGINATION = 10

TWITTER_USERNAME="avances123"
TWITTER_CARDS=True
USE_OPEN_GRAPH=True


GITHUB_USER="avances123"
#GITHUB_SHOW_USER_LINK=True
GITHUB_REPO_COUNT=3



BOOTSTRAP_THEME = "flatly"
PYGMENTS_STYLE = "monokai"
CC_LICENSE="BY-NC-SA"
DISPLAY_TAGS_ON_SIDEBAR=False
#TWITTER_WIDGET_ID="528594645018632192"
AVATAR="https://lh5.googleusercontent.com/-arGkRvO4W7M/AAAAAAAAAAI/AAAAAAAAeDE/rLBXQaVKRbE/s120-c/photo.jpg"
SHOW_ABOUTME=True
ADDTHIS_PROFILE="ra-5455185a630e0def"
DISPLAY_ARTICLE_INFO_ON_INDEX=True

