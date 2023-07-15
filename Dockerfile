FROM docker.io/python:3.11.4-alpine3.18

RUN apk add --no-cache git

WORKDIR /app

COPY . .

RUN mkdir output
RUN pip3 install -r requirements.txt
RUN pip3 install --editable .

WORKDIR /app/output

ENTRYPOINT ["icsmerger"]
CMD ["-h"]