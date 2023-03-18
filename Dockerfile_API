FROM guessink/guessink-api:guessink-api-base-image

RUN apk del build_deps

WORKDIR /app

COPY . /app

ENV FLASK_APP=index.py

EXPOSE 8080

CMD ["python3", "index.py"]