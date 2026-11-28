# Dependabot keeps the -alpineX.Y suffix; bump it by hand when a new Alpine release is out.
# The base image is repeated in the build and production stages so Dependabot finds both.
FROM docker.io/python:3.15.2-alpine3.24 AS build

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

FROM docker.io/python:3.15.2-alpine3.24 AS production

# Runtime dependencies and the wheel only: no git, .git, tests or source tree.
# Bind mounts keep requirements.txt and the wheel out of the image layers.
RUN --mount=type=bind,from=build,source=/dist,target=/dist \
    --mount=type=bind,source=requirements.txt,target=/requirements.txt \
    pip3 install --no-cache-dir -r /requirements.txt /dist/*.whl

# Run as a dedicated non-root user. The numeric UID lets Kubernetes runAsNonRoot verify it.
RUN addgroup -S -g 10001 icsmerger \
    && adduser -S -D -H -u 10001 -G icsmerger icsmerger \
    && mkdir -p /app/output \
    && chown 10001:10001 /app/output

WORKDIR /app/output
USER 10001:10001

ENTRYPOINT ["icsmerger"]
CMD ["-h"]
