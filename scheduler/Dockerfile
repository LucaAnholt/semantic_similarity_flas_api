FROM python:3-alpine 

RUN python -m pip install schedule 

WORKDIR /app

COPY . /app

CMD ["python3", "schedule_url_answers.py"]
