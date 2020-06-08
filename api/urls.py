from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.models import Permission
from api.views import APIRoot, UserProfile, login #, UserView

#from rest_framework import routers

try:
    admin.site.register(Permission)
except:
    pass

admin.autodiscover()

#router=routers.SimpleRouter()
#router.register(r'accounts', UserView, 'list')

urlpatterns = patterns('',
    #url(r'^api/', include(router.urls)),
    # Django Rest Login Urls
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Queue Application
    url(r'^queue/', include('cybercom_queue.urls')),
    url(r'^data_store/',include('data_store.urls')),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^obis/',include('obis.urls')),
    # Main Project View - Customize depending on what Apps are enabled
    url(r'^$', APIRoot.as_view()),
    url(r'^/\.(?P<format>(api|json|jsonp|xml|yaml))/$', APIRoot.as_view()),
    # User Profile
    url(r'^user/',UserProfile.as_view(),name='user-list'),
    url(r'^login', login),
    # Authentication
    url(r'^register/$', TemplateView.as_view(template_name="register.html"), name='register'),
    url(r'^verify/$', TemplateView.as_view(template_name="verify.html"), name='verify'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # Admin Urls
    url(r'^admin/', include(admin.site.urls))
)
