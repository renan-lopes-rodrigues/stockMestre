FROM python:3.11

WORKDIR /www

COPY ./ /www/
RUN apt-get update
# RUN apt  install build-dep python-psycopg2
# RUN pip install psycopg2-binary

RUN pip install --no-cache-dir --upgrade -r /www/requirements.txt

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--reload" ]