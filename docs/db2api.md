## Database Table/View to API

This documentation is a demonstration of how to create a view or table and move the data to the API.

### Creation of View (Example)

1. Create SQL query and run within the database.
2.  Generate auto model Creation
    
    * Log into Dev/Prod system.
    * Access the API docker container

    docker ps
    docker exec -it obis_api /bin/bash
    ./manage.py inspectdb --database obis > misc/20180111model.py

3. Exit docker container (exit)

### Model Creation

1. The files that you just created are located in /opt/obis/api_code/
2. Copy the class model from the file
  * Add class to /opt/obis/api_code/obis/models.py
  * [Current models.py](https://github.com/oklahoma-biological-survey/obis_api/blob/master/obis/models.py)

### View Creation

1. Import model into [views.py](https://github.com/oklahoma-biological-survey/obis_api/blob/master/obis/views.py)
2. Create class for Table or VIEW
  * Use the appropriate base Class
    * obisTableViewSet for Tables
    * obisViewViewSet for View
3. Add Model and queryset to Class
  * add search fields and ordering fields
  * [filters](https://github.com/oklahoma-biological-survey/obis_api/blob/master/obis/filters.py)
  * [serializers](https://github.com/oklahoma-biological-survey/obis_api/blob/master/obis/serializer.py)

### URL Creation

1. Import ViewSet to [urls.py](https://github.com/oklahoma-biological-survey/obis_api/blob/master/obis/urls.py)
2. Register model and setup url that will be used to access data

### Add to Main API view for link Access

1. [api/views.py](https://github.com/oklahoma-biological-survey/obis_api/blob/286608145977a27617e46c3f449606c912297000/api/views.py#L49)
2. Use the name of the url that you assigned in URL Creation
3. reverse('<Name of URL>-list',request=request)

### Restart API

1. /opt/obis/run/appContainerKill
2. /opt/obis/run/cybercom_up
3. docker ps
4. make sure api is up and running.
5. If obis_api is not running. Check /opt/obis/log/api.log
