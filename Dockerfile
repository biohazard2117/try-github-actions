FROM python:3.10.11-alpine

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY . code
WORKDIR /code

# migrate the changes
RUN python manage.py migrate

# collect all the static files 
RUN python manage.py collectstatic --no-input

EXPOSE 8000

# runs the production server
# ENTRYPOINT ["python", "manage.py"]
# CMD ["runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "test", "test.wsgi:application"]