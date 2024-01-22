FROM python:3.10-slim-bullseye

RUN pip install --no-cache-dir Flask gunicorn

COPY . /

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "app:app"]