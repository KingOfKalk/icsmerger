FROM docker.io/python:3.12.3-alpine3.18 as build

RUN apk add --no-cache git

WORKDIR /app

COPY . .

RUN mkdir output
RUN pip3 install -r requirements.txt
RUN pip3 install --editable .

FROM build as test
RUN pip3 install -r requirements_dev.txt
RUN pytest --no-cov .

FROM build as production
WORKDIR /app/output

ENTRYPOINT ["icsmerger"]
CMD ["-h"]