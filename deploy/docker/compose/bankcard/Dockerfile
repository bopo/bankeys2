FROM alpine:3.6
ENV PYTHONUNBUFFERED 1

COPY ./compose/bankcard/standard/pip.conf /root/.pip/pip.conf
COPY ./compose/bankcard/standard/app/requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY ./compose/bankcard/standard/app /app

WORKDIR /app

ENTRYPOINT ["python", "server.py"]
