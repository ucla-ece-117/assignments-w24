FROM python:3.10-slim-bullseye

RUN pip install --no-cache-dir Flask Flask-SQLAlchemy gunicorn

COPY . /

RUN mkdir -p /instance

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:80", "app:app"]