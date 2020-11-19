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
from django.conf.urls import include, path, url
from django.contrib import admin
from django.contrib.auth.models import Permission
from django.urls import re_path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from api import views

try:
    admin.site.register(Permission)
except:
    pass

admin.autodiscover()

schema_view = get_schema_view(
    openapi.Info(
        title            = 'OBIS API',
        default_version  = 'v2.0',
        description      = 'REST API for the Oklahoma Biodiversity Information System.',
        terms_of_service = 'https://www.google.com/policies/terms/',
        contact          = openapi.Contact(email='twalker1998@gmail.com'),
        license          = openapi.License(name='BSD License')
    ),
    public             = True,
    permission_classes = (permissions.AllowAny,),
)

urlpatterns = [
    # Admin URLs
    url(r'^admin/', admin.site.urls),

    # Django Rest Login URLs
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), # TODO: might not need

    # OBIS Application URLs
    url(r'^obis/',include('obis.urls')),

    # Main Project View - Customize depending on what Apps are enabled
    url(r'^$', views.APIRoot.as_view()),
    url(r'^\.(?P<format>(api|json))/$', views.APIRoot.as_view()),

    # User Profile
    url(r'^user/', views.UserProfile.as_view(), name='user-list'),
    url(r'^login', views.login),

    # Authentication
    url(r'^register/$', TemplateView.as_view(template_name="register.html"), name='register'), # TODO: might not need
    url(r'^verify/$', TemplateView.as_view(template_name="verify.html"), name='verify'), # TODO: might not need
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

    # Yasg
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('openapi/', TemplateView.as_view(template_name='swagger-ui/dist/index.html')),
]
