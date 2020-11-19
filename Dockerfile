FROM python:3.9
MAINTAINER Tyler Walker <twalker1998@gmail.com>

RUN apt-get update && apt-get install -y vim libpq-dev python-dev

COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements

EXPOSE 8080
WORKDIR /usr/src/app
CMD ["gunicorn", "--config=gunicorn.py", "api.wsgi:application"]
