FROM python:3.9-alpine

RUN apk add --no-cache git

WORKDIR /app

COPY . .

RUN mkdir output
RUN pip3 install -r requirements.txt
RUN pip3 install --editable .

WORKDIR /app/output

ENTRYPOINT ["icsmerger"]
CMD ["-h"]