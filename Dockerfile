
FROM python:3.8
ENV POSTGRES_DB=respond
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=235678
ENV POSTGRES_HOST=localhost

RUN apt-get update && apt-get install -y libpq-dev
RUN pip install psycopg2


WORKDIR /app


COPY requirements.txt .


RUN pip install -r requirements.txt


COPY .. .


RUN python manage.py migrate


CMD python manage.py runserver 0.0.0.0:8000