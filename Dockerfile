FROM python:3.7
MAINTAINER Nima Maghsoodi
ADD . /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install django-tables2
RUN pip3 install pandas
RUN pip3 install datetime
RUN pip3 install whitenoise
EXPOSE 8000
CMD exec gunicorn ReconDashboard.wsgi:application --bind 0.0.0.0:8000 --workers 3
