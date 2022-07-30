FROM python:3.10.5-slim

WORKDIR /django_hillel
COPY ./ ./

RUN pip install -U pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]