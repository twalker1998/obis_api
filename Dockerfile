FROM python:3
MAINTAINER Mark Stacy <markstacy@ou.edu>

RUN apt-get update && apt-get install -y vim

COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["gunicorn", "--config=gunicorn.py", "api.wsgi:application"]
