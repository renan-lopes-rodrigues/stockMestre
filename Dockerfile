FROM python:3.11

WORKDIR /www

COPY ./ /www/
RUN apt-get update

RUN pip install --no-cache-dir --upgrade -r /www/requirements.txt

RUN chmod +x entrypoint.sh