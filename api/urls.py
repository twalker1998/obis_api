from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.models import Permission
from .views import APIRoot, UserProfile, login #, UserView

#from rest_framework import routers

try:
    admin.site.register(Permission)
except:
    pass

admin.autodiscover()

#router=routers.SimpleRouter()
#router.register(r'accounts', UserView, 'list')

urlpatterns = [
    #url('api/', include(router.urls)),
    # Django Rest Login Urls
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Queue Application
    url('queue/', include('cybercom_queue.urls')),
    url('data_store/',include('data_store.urls')),
    url('catalog/', include('catalog.urls')),
    url('obis/',include('obis.urls')),
    # Main Project View - Customize depending on what Apps are enabled
    url('$', APIRoot.as_view()),
    url('/\.(?P<format>(api|json|jsonp|xml|yaml))/$', APIRoot.as_view()),
    # User Profile
    url('user/',UserProfile.as_view(),name='user-list'),
    url('login', login),
    # Authentication
    url('register/$', TemplateView.as_view(template_name="register.html"), name='register'),
    url('verify/$', TemplateView.as_view(template_name="verify.html"), name='verify'),
    url('rest-auth/', include('rest_auth.urls')),
    url('rest-auth/registration/', include('rest_auth.registration.urls')),
    # Admin Urls
    url('admin/', admin.site.urls)
]
