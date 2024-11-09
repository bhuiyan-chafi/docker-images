# Use an official Python runtime as a parent image
FROM python:3.9.20-slim
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy Pipfile and Pipfile.lock to the working directory
COPY Pipfile Pipfile.lock /app/
COPY requirements.txt /app/

# Install pipenv and project dependencies
RUN pip install --upgrade pip && pip install pipenv && pipenv install --system --deploy && pip install -r requirements.txt

# Copy the Django project into the container
COPY . /app

# Expose port 8000 to allow access to the Django app
EXPOSE 8000

# Start Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]