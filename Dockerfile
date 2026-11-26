# Dependabot keeps the -alpineX.Y suffix; bump it by hand when a new Alpine release is out.
FROM docker.io/python:3.14.10-alpine3.24 AS build

RUN apk add --no-cache git

WORKDIR /app

COPY . .

RUN mkdir output
RUN pip3 install -r requirements.txt
RUN pip3 install --editable .

FROM build AS test
RUN pip3 install -r requirements_dev.txt
RUN pytest --no-cov .

FROM build AS production
WORKDIR /app/output

ENTRYPOINT ["icsmerger"]
CMD ["-h"]
