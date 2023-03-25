FROM python:3-alpine 

RUN python -m pip install schedule 

WORKDIR /app

COPY . /app

RUN mkdir -p /app/data

CMD ["python3", "schedule_url_answers.py"]
