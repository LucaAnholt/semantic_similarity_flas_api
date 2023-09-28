FROM guessink/guessink-api:guessink-api-base-image

WORKDIR /app

COPY . /app

RUN pip install gunicorn

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "index:app"]