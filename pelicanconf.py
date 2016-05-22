#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Johan Carlin'
SITENAME = u'Johan Carlin'
SITEURL = ''
DEFAULT_DATE_FORMAT = '%d %B %Y'
USE_FOLDER_AS_CATEGORY = True
DEFAULT_DATE = 'fs'
TYPOGRIFY = True
THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'lumen'
PLUGINS = ['pelican_gist','ipynb.markup']
MARKUP = ('md','ipynb')
PYGMENTS_STYLE = 'borland'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

GITHUB_URL = 'https://github.com/jooh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Love lab', 'http://www.ucl.ac.uk/lovelab'),
        ('Kriegeskorte lab',
            'http://www.mrc-cbu.cam.ac.uk/our-research/kriegeskorte'),
        ('Gardner lab', 'http://gru.stanford.edu'))

# Social widget
SOCIAL = (('code', 'https://github.com/jooh'),
          ('rants', 'https://twitter.com/johancarlin'),
          ('python packages','https://anaconda.org/jcarlin'),
          ('publications','https://www.mendeley.com/profiles/johan-carlin'),
          ('long reads','https://getpocket.com/@idoru'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
