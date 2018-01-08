from django.contrib import admin
from django.apps import apps

app = apps.get_app_config('obis')

#for model_name, model in app.models.items():
#    admin.site.register(model)

from django.contrib.auth.management import create_permissions

create_permissions(app)
