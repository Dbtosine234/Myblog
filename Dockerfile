FROM python:3.9

RUN mkdir /blogemmax

WORKDIR /blogemmax

COPY . /blogemmax/

RUN pip install -r requirements.txt
