# Changelog

This is a list of notable changes to the project.

## [v1.0.1] - 2023-07-7

- Bumps click from 8.1.3 to 8.1.4. #23
- Bumps urllib3 from 1.26.14 to 2.0.3. #18, #20
- Bumps pytest from 7.3.1 to 7.4.0. #21, #22
- Implements GitHub Actions based Dependabot Version Updates . #17, #19

## [v1.0.0] - 2023-06-03

- Updates dependencies, including dependencies for development. #15
- Updates Dependabot settings. #14
- Adds Dependabot version updates. #13
- Bumps requests from 2.28.2 to 2.31.0 #12
- Adds 2nd level dependcies to requirements list. #11
- Removes manual trigger from Github workflow for building Docker images. #10
- Enhances CodeQL workflow. #9
- Upgrades CI-QA-Pipeline to run also on PR. #8
- Updates change log.d #7
- Sets correct Python versions for GitHub worflows. #6
- Enhances GitHUb workflows. #5

## [v0.0.8] - 2023-02-11

- Prepares for ics v0.9.0.
  See https://github.com/ics-py/ics-py/commit/f64c112dbacb2a49ad2ca53de8c579b5710ce992.

## [v0.0.7] - 2023-02-11

- Upgrades requirements and dev requirements.
- Upgrades Docker base image to python 3.11-alpine.

## [v0.0.6] - 2023-02-11

- Updates GitHub Action [docker-image.yml](.github/workflows/docker-image.yml) to support multi-platform builds.

## [v0.0.5] - 2022-02-10

- Optimized Docker image to use ENTRYPOINT and CMD better.
- Set CWD to /app/out in Docker image, so creating merged ICS files in a volume is easier.
- Updated documentation.
- Removed demo GitHub action.

## [v0.0.4] - 2022-02-09

- Added support for Docker.

## [v0.0.3] - 2021-06-15

- Implemented exception handling for HTTPS rqequests.

## [v0.0.2] - 2021-06-15

- Refactored project structure.
- Refactired unit tests into single files.
- Implemented option to ignore HTTP status codes equal or greater 400.

## [v0.0.1] - 2021-06-12

- Started project.
