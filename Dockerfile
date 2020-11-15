FROM python:3.9
MAINTAINER Mark Stacy <markstacy@ou.edu>

RUN apt-get update && apt-get install -y vim libpq-dev python-dev

COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt

EXPOSE 8080
WORKDIR /usr/src/app
CMD ["gunicorn", "--config=gunicorn.py", "api.wsgi:application"]
