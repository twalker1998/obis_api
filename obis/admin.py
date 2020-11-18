from django.apps import apps
from django.contrib.auth.management import create_permissions

app = apps.get_app_config('obis')
create_permissions(app)
