FROM python:alpine3.15

RUN addgroup -S app && \
    adduser -S app -G app && \
    mkdir -p /app && \
    chown -R app:app /app

USER app
WORKDIR /app

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "api.py" ]
