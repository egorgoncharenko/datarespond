FROM python:3.8

# Install PostgreSQL
RUN apt-get update && apt-get install -y postgresql

ENV POSTGRES_DB=respond
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=235678
ENV POSTGRES_HOST=localhost

RUN apt-get install -y libpq-dev
RUN pip install psycopg2

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY .. .

# Start PostgreSQL service
RUN service postgresql start

# Create the necessary PostgreSQL database and user
RUN su - postgres -c "psql -c 'CREATE DATABASE respond;'"
RUN su - postgres -c "psql -c 'CREATE USER postgres WITH PASSWORD '235678';'"
RUN su - postgres -c "psql -c 'GRANT ALL PRIVILEGES ON DATABASE respond TO postgres;'"

RUN python manage.py migrate

CMD python manage.py runserver 0.0.0.0:8000