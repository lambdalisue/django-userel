#!/usr/bin/env python
# vim: set fileencoding=utf8:
"""
Userel

A extend ForeignKey field for user relation.

AUTHOR:
    lambdalisue[Ali su ae] (lambdalisue@hashnote.net)
    
Copyright:
    Copyright 2011 Alisue allright reserved.

License:
    Licensed under the Apache License, Version 2.0 (the "License"); 
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unliss required by applicable law or agreed to in writing, software
    distributed under the License is distrubuted on an "AS IS" BASICS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
__AUTHOR__ = "lambdalisue (lambdalisue@hashnote.net)"
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module

import backends

settings.USEREL_BACKEND = getattr(settings, 'USEREL_BACKEND', backends.UserelDefaultBackend)

def load_backend(path):
    """load userel backend from string path"""
    i = path.rfind('.')
    module ,attr = path[:i], path[i+1:]
    try:
        mod = import_module(module)
    except ImportError, e:
        raise ImproperlyConfigured('Error importing userel backend %s: "%s"' % (path, e))
    except ValueError, e:
        raise ImproperlyConfigured('Error importing userel backend. Is USEREL_BACKEND a correctly defined?')
    try:
        cls = getattr(mod, attr)
    except AttributeError:
        raise ImproperlyConfigured('Module "%s" does not define a "%s" userel backend' % (module, attr))
    
    if not hasattr(cls, 'get_user'):
        raise ImproperlyConfigured('Error userel backend must have "get_user" method Please define it in %s.' % cls)
    return cls()

def get_backend_class():
    """get userel backend"""
    backend = settings.USEREL_BACKEND
    if isinstance(backend, basestring):
        return load_backend(backend)
    elif isinstance(backend, object) and hasattr(backend, 'get_user'):
        return backend
    else:
        raise ImproperlyConfigured('Error userel backend must have "get_user" method Please define it in %s.' % backend)

def get_backend():
    backend_class = get_backend_class()
    return backend_class()
