Oklahoma Biological Information System Django Application

Install application

1. Add "obis" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'obis',
    ]
2. Include the obis URLconf in your project urls.py like this::

    url(r'^obis/', include('obis.urls')),

3. Update api_config.py in cybercommons config folder
	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	    },
	    'obis':{
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'HOST':'ip address of db server',
		'NAME': 'obis',
		'USER': 'user',
		'PASSWORD': 'password',
	    },
	}

	DATABASE_ROUTERS = ['obis.database_router.obisRouter',]
4. Update api/views.py to update the main rest api 
        class APIRoot(APIView):
	    permission_classes = ( IsAuthenticatedOrReadOnly,)
	    def get(self, request,format=None):
		return Response({
		    'Queue': {'Tasks': reverse('queue-main', request=request),
			      'Tasks History': reverse('queue-user-tasks',request=request)},
		    'Catalog': {'Data Source':reverse('catalog-list',request=request)},
		    'Data Store': {'OBIS':[reverse('acctax-list',request=request),
					   reverse('comtax-list',request=request),
					   reverse('syntax-list',request=request),],
				    'Mongo':reverse('data-list',request=request)},
		    'User Profile': {'User':reverse('user-list',request=request)}
		})
