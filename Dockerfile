# Указываем базовый образ для контейнера
FROM python:3.9

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


WORKDIR /datarespond


COPY requirements.txt .


RUN pip install -r requirements.txt


COPY . .


ENV DB_NAME=mydatabase
ENV DB_USER=myuser
ENV DB_PASSWORD=mypassword
ENV DB_HOST=db
ENV DB_PORT=5432


RUN python manage.py migrate

# Запускаем сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]