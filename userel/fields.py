#!/usr/bin/env python
# vim: set fileencoding=utf8:
"""
short module explanation


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
from django.db import models

class UserelField(models.ForeignKey):
    """Extend ForeignKey field for user which support ``auto_now`` and ``auto_now_add``"""
    def __init__(self, verbose_name=None, name=None, auto_now=False, auto_now_add=False, to=None, **kwargs):
        from . import get_backend
        self._backend = get_backend()
        self.auto_now, self.auto_now_add = auto_now, auto_now_add
        if auto_now or auto_now_add:
            kwargs['editable'] = False
            kwargs['blank'] = True
        if not to:
            to = self._backend._get_user_model()
        kwargs['verbose_name'] = verbose_name
        kwargs['name'] = name
        super(UserelField, self).__init__(to=to, **kwargs)

    def pre_save(self, model_instance, add):
        if self.auto_now or (self.auto_now_add and add):
            value = self._backend.get_user()
            if isinstance(value, self.rel.to):
                if self.auto_now or not getattr(model_instance, self.attname, None):
                    setattr(model_instance, self.attname, value.pk)
                    return value.pk
        # Non auto_now/auto_now_add or anonymous user is working
        return super(UserelField, self).pre_save(model_instance, add)
