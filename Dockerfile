# Dependabot keeps the -alpineX.Y suffix; bump it by hand when a new Alpine release is out.
# The base image is repeated in the build and production stages so Dependabot finds both.
FROM docker.io/python:3.14.10-alpine3.24 AS build

# git and .git are needed at build time only: setuptools_scm derives the version from the tag.
RUN apk add --no-cache git

WORKDIR /app

COPY . .

# requirements_dev.txt pins the build frontend (and the test tools the test stage reuses).
RUN pip3 install -r requirements.txt -r requirements_dev.txt
RUN python -m build --wheel --outdir /dist

FROM build AS test
RUN pip3 install --editable .
RUN pytest --no-cov .

FROM docker.io/python:3.14.10-alpine3.24 AS production

WORKDIR /app

# Runtime dependencies and the wheel only: no git, .git, tests or source tree.
COPY requirements.txt .
COPY --from=build /dist /dist
RUN pip3 install --no-cache-dir -r requirements.txt /dist/*.whl \
    && rm -rf /dist requirements.txt

WORKDIR /app/output

ENTRYPOINT ["icsmerger"]
CMD ["-h"]
