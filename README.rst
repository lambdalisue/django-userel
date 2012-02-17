Userel is a extend ForeignKey for User model. It add ``auto_now`` and ``auto_now_add`` for setting current
access user automatically.

Install
===========================================
::

	sudo pip install django-userel

or::

    sudo pip install git+https://github.com/lambdalisue/django-userel.git#egg=django-userel


How to Use
==========================================

1.  Append 'userel' to ``INSTALLED_APPS``

2.  Add 'userel.middlewares.UserelDefaultBackendMiddleware' to your ``MIDDLEWARE_CLASSES``
    if you use default userel backend


Example mini blog app
=========================================

``models.py``::
	
	from django.db import models
	from django.contrib.auth.models import User

	from userel.fields import UserelField
	
	class Entry(models.Model):
		PUB_STATES = (
			('public', 'public entry'),
			('protected', 'login required'),
			('private', 'secret entry'),
		)
		pub_state = models.CharField('publish status', choices=PUB_STATES)
		title = models.CharField('title', max_length=140)
		body = models.TextField('body')

        created_by = UserelField('created by', related_name='entries_create', auto_now_add=True)
        updated_by = UserelField('updated_by', related_name='entries_update', auto_now=True)


Settings
================

USEREL_BACKEND
    Class or string path of backend. the backend is used to determine user when object is created/updated.


Backend
==============
The default backend use ``thread_locals`` storategy to get current request in signal call.

If you want to change the strategy or whatever, create your own backend.

A backend is a class which have ``get_user`` method to determine current user.

UserelDefaultBackend
    Default backend. This backend return None when no request found or AnonymousUser create/update object.

UserelSystemUserBackend
    System user backend. This backend return system user when no request found or AnonymousUser create/update object.

    system user is determined with ``get_system_user`` method and default is ``User.objects.get(pk=1)``
