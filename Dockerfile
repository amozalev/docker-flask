FROM python:3.6.4-alpine3.7

RUN apk update
RUN mkdir /docker-flask
WORKDIR /docker-flask
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN addgroup -g 1000 -S flask_user && \
    adduser -u 1000 -S flask_user -G flask_user && \
    chown -R flask_user:flask_user $(pwd)
USER flask_user
ADD . .
EXPOSE 8000
#CMD ["python", "manage.py"]
ENTRYPOINT ["/usr/local/bin/gunicorn", "--config", "gunicorn.conf.py", "manage:app"]