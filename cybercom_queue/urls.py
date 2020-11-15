__author__ = 'mstacy'
from django.conf.urls import url
from django.contrib import admin
from .views import Run, Queue, UserTasks, UserResult,flushMemcache
from rest_framework.urlpatterns import format_suffix_patterns

admin.autodiscover()

urlpatterns = [
    url('run/(?P<task_name>[-\w .]+)/$', Run.as_view(), name='run-main'),
    url('task/(?P<task_id>[-\w]+)/$', UserResult.as_view(), name='queue-task-result'),
    url('usertasks/$', UserTasks.as_view(), name='queue-user-tasks'),
    url('memcache',flushMemcache.as_view(), name= 'flush-memcache'),
    url('$', Queue.as_view(), name="queue-main")
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json', 'jsonp', 'xml', 'yaml'])
