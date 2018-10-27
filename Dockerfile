FROM python:2.7-alpine

LABEL maintainer="pan.luo@ubc.ca"

WORKDIR /src

RUN pip install --no-cache-dir --disable-pip-version-check csvkit==0.9.2

ADD . /src

EXPOSE 8080

CMD ["python", "isw.py"]