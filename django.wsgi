#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

activate_this = '/home/hosting_leidenit/s_env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, '/home/hosting_leidenit/s_env/lib/site-packages')
sys.path.insert(0, '/home/hosting_leidenit/projects/slideshot')

os.environ['DJANGO_SETTINGS_MODULE'] = 'slideshot.settings'

from slideshot.wsgi import application
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()