# Используем базовый образ Python
FROM python:3.10

# Устанавливаем переменную окружения для запуска в неинтерактивном режиме
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем requirements.txt в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /app/

# Команда для запуска Django-приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]