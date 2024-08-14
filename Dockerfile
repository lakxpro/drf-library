FROM python:3.11-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    netcat \
    && rm -rf /var/lib/apt/lists/*

# Install pip requirements
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the Django project into the Docker image
COPY . /app/

# Run migrations and custom management commands
RUN python manage.py migrate
RUN python manage.py fake_authors
RUN python manage.py fake_books

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]