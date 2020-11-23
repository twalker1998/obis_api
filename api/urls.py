"""
api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import Permission
from django.views.generic import TemplateView

from api import views

try:
    admin.site.register(Permission)
except:
    pass

admin.autodiscover()

urlpatterns = [
    # Grappelli URLs
    url(r'^grappelli/', include('grappelli.urls')),

    # Admin URLs
    url(r'^admin/', admin.site.urls),

    # OBIS Application URLs
    url(r'^obis/',include('obis.urls')),

    # Main Project View - Customize depending on what Apps are enabled
    url(r'^$', views.APIRoot.as_view()),
    url(r'^\.(?P<format>(api|json))/$', views.APIRoot.as_view()),

    # User Profile
    url(r'^user/', views.UserProfile.as_view(), name='user-list'),
    
    # Authentication
    url(r'^register/$', TemplateView.as_view(template_name="register.html"), name='register'), # TODO: might not need
    url(r'^verify/$', TemplateView.as_view(template_name="verify.html"), name='verify'), # TODO: might not need
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]
