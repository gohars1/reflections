#Dockerfile

# The image we want to base our container on
FROM python:3.10.6

# Cache installed deps between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY . code
WORKDIR /code

EXPOSE 8000

ENTRYPOINT ["python", "reflections/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]