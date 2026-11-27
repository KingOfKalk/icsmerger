# Changelog

This is a list of notable changes to the project.

## [1.2.2](https://github.com/KingOfKalk/icsmerger/compare/v1.2.1...v1.2.2) (2026-11-27)


### Bug Fixes

* **docker:** build a slim production stage ([#231](https://github.com/KingOfKalk/icsmerger/issues/231)) ([7f41be0](https://github.com/KingOfKalk/icsmerger/commit/7f41be01e0d230febaad59298de5fed612c07a72))
* **docker:** bump base image to python 3.14 on alpine 3.24 ([#226](https://github.com/KingOfKalk/icsmerger/issues/226)) ([ced0957](https://github.com/KingOfKalk/icsmerger/commit/ced09575313ee89f9bef11636e338a0add1a1a1e))
* **merge:** handle HTTP errors, timeouts and encoding ([#229](https://github.com/KingOfKalk/icsmerger/issues/229)) ([25c5fe0](https://github.com/KingOfKalk/icsmerger/commit/25c5fe0dac89e96bfa0571000ae4759f5c214ea4))


### Documentation

* **readme:** fix badges, image name and paths ([#225](https://github.com/KingOfKalk/icsmerger/issues/225)) ([3459d78](https://github.com/KingOfKalk/icsmerger/commit/3459d78613a71f450ac27d01c3babaa99d363132))


### Build System

* **packaging:** remove dead config and keep tests out of the wheel ([#227](https://github.com/KingOfKalk/icsmerger/issues/227)) ([52f21dd](https://github.com/KingOfKalk/icsmerger/commit/52f21dda8fe17ff1b2a2145e9f02e7e3c765c2fc))


### Continuous Integration

* **workflows:** least-privilege App tokens and job timeouts ([#228](https://github.com/KingOfKalk/icsmerger/issues/228)) ([e16d4b5](https://github.com/KingOfKalk/icsmerger/commit/e16d4b54d6541dd5fac5a1207f033760edb846aa))

## [1.2.1](https://github.com/KingOfKalk/icsmerger/compare/v1.2.0...v1.2.1) (2026-11-26)


### Bug Fixes

* **deps:** Bump idna from 3.11 to 3.15 ([#207](https://github.com/KingOfKalk/icsmerger/issues/207)) ([8fb2d44](https://github.com/KingOfKalk/icsmerger/commit/8fb2d44a383a61e3f197633dbefb204c33338bde))
* **deps:** Bump requests from 2.32.5 to 2.33.0 ([#209](https://github.com/KingOfKalk/icsmerger/issues/209)) ([a245583](https://github.com/KingOfKalk/icsmerger/commit/a2455835bffb45d956d8094a5c587884ed6e0e35))
* **deps:** Bump urllib3 from 2.6.3 to 2.8.0 ([#208](https://github.com/KingOfKalk/icsmerger/issues/208)) ([f1f2e26](https://github.com/KingOfKalk/icsmerger/commit/f1f2e267e0fac59d141570caaa99273a8e4fd0db))


### Chores

* **deps-dev:** Bump pytest from 9.0.2 to 9.0.3 ([#210](https://github.com/KingOfKalk/icsmerger/issues/210)) ([9e5ae6b](https://github.com/KingOfKalk/icsmerger/commit/9e5ae6b48e55e025a9cf61c97228cea7079d0ee9))

## [1.2.0](https://github.com/KingOfKalk/icsmerger/compare/v1.1.0...v1.2.0) (2026-11-26)


### Features

* **github:** Add Python 3.14 to GitHub workflows. ([#164](https://github.com/KingOfKalk/icsmerger/issues/164)) ([d968f36](https://github.com/KingOfKalk/icsmerger/commit/d968f36fa33a58a5938598d025e704999cb4fef5))


### Bug Fixes

* **deps:** Bump attrs from 25.4.0 to 26.1.0 ([#197](https://github.com/KingOfKalk/icsmerger/issues/197)) ([12d50e0](https://github.com/KingOfKalk/icsmerger/commit/12d50e053bc253759835a5df8772fd1a552f1e07))
* **deps:** Bump certifi from 2026.1.4 to 2026.11.20 ([#203](https://github.com/KingOfKalk/icsmerger/issues/203)) ([cc3f4e4](https://github.com/KingOfKalk/icsmerger/commit/cc3f4e48f161084310cd2db691c4f7abbbda6687))
* **deps:** Bump charset-normalizer from 3.4.4 to 3.5.3 ([#204](https://github.com/KingOfKalk/icsmerger/issues/204)) ([9e8c664](https://github.com/KingOfKalk/icsmerger/commit/9e8c664496bba0dc947ba431d1791b733bdcba08))
* **deps:** pin TatSu to 5.15.1 ([#195](https://github.com/KingOfKalk/icsmerger/issues/195)) ([26e1d7c](https://github.com/KingOfKalk/icsmerger/commit/26e1d7ca5dc6843f89cd6d0aa67cc973ef505cf3))


### Continuous Integration

* adopt release-please, Dependabot auto-merge and hardened workflows ([#201](https://github.com/KingOfKalk/icsmerger/issues/201)) ([c529843](https://github.com/KingOfKalk/icsmerger/commit/c5298434ace1b6b6976b9436e50e0a0234bc01d1))


### Chores

* **deps-dev:** Bump build from 1.2.2.post1 to 1.3.0 ([#150](https://github.com/KingOfKalk/icsmerger/issues/150)) ([dd6d3e1](https://github.com/KingOfKalk/icsmerger/commit/dd6d3e166c4cb5d23a4f4168172240c325d4737e))
* **deps-dev:** Bump build from 1.3.0 to 1.4.0 ([#186](https://github.com/KingOfKalk/icsmerger/issues/186)) ([3160729](https://github.com/KingOfKalk/icsmerger/commit/31607293ae8d099ed9e7a5da1c777fee0ee4d370))
* **deps-dev:** Bump build from 1.4.0 to 1.6.1 ([#205](https://github.com/KingOfKalk/icsmerger/issues/205)) ([21576a6](https://github.com/KingOfKalk/icsmerger/commit/21576a6551a82e323c884ad2a2aab90f11640270))
* **deps-dev:** Bump pytest from 8.4.1 to 8.4.2 ([#155](https://github.com/KingOfKalk/icsmerger/issues/155)) ([aaf0d9c](https://github.com/KingOfKalk/icsmerger/commit/aaf0d9cbe6a5018faaed38a688c6fab70363200f))
* **deps-dev:** Bump pytest from 8.4.2 to 9.0.1 ([#171](https://github.com/KingOfKalk/icsmerger/issues/171)) ([1b02d93](https://github.com/KingOfKalk/icsmerger/commit/1b02d93b6764c7d50ab67c7fc1bb2389525f9bd5))
* **deps-dev:** Bump pytest from 9.0.1 to 9.0.2 ([#177](https://github.com/KingOfKalk/icsmerger/issues/177)) ([63d6e0b](https://github.com/KingOfKalk/icsmerger/commit/63d6e0b4c22313f6029017018925a66274e1e8d8))
* **deps-dev:** Bump pytest-cov from 6.2.1 to 7.0.0 ([#158](https://github.com/KingOfKalk/icsmerger/issues/158)) ([ee0eed4](https://github.com/KingOfKalk/icsmerger/commit/ee0eed4d83d032dba13fcd1aaa09310fed8cd644))
* **deps-dev:** Bump pytest-cov from 7.0.0 to 7.1.0 ([#198](https://github.com/KingOfKalk/icsmerger/issues/198)) ([3cf6665](https://github.com/KingOfKalk/icsmerger/commit/3cf66655dd37b54aa3f1d08b3f4a0903670f51da))
* **deps:** Bump actions/checkout from 4 to 5 ([#153](https://github.com/KingOfKalk/icsmerger/issues/153)) ([5956e98](https://github.com/KingOfKalk/icsmerger/commit/5956e98f13098a08fb5fe906453395374b88b682))
* **deps:** Bump actions/checkout from 5 to 6 ([#173](https://github.com/KingOfKalk/icsmerger/issues/173)) ([c9918d3](https://github.com/KingOfKalk/icsmerger/commit/c9918d32ce0bdd2c7a41d7d0ca14c76f474fcdf2))
* **deps:** Bump actions/setup-python from 5 to 6 ([#156](https://github.com/KingOfKalk/icsmerger/issues/156)) ([79d16a2](https://github.com/KingOfKalk/icsmerger/commit/79d16a2915427632daba710510fbe42991c33dc5))
* **deps:** Bump actions/upload-artifact from 4 to 5 ([#169](https://github.com/KingOfKalk/icsmerger/issues/169)) ([c35e8f2](https://github.com/KingOfKalk/icsmerger/commit/c35e8f2b78342325915d7a80bbc25bdaad906cfb))
* **deps:** Bump actions/upload-artifact from 5 to 6 ([#181](https://github.com/KingOfKalk/icsmerger/issues/181)) ([a4fb813](https://github.com/KingOfKalk/icsmerger/commit/a4fb81394e19afff5660421f729407ea835f1554))
* **deps:** Bump arrow from 1.3.0 to 1.4.0 ([#168](https://github.com/KingOfKalk/icsmerger/issues/168)) ([e8ccfd8](https://github.com/KingOfKalk/icsmerger/commit/e8ccfd89a6a57d8379c9d440d1335d91315b5743))
* **deps:** Bump attrs from 25.3.0 to 25.4.0 ([#162](https://github.com/KingOfKalk/icsmerger/issues/162)) ([28db129](https://github.com/KingOfKalk/icsmerger/commit/28db12945609d2b8c1bb04e8ebdd877d94ab0347))
* **deps:** Bump certifi from 2025.10.5 to 2025.11.12 ([#172](https://github.com/KingOfKalk/icsmerger/issues/172)) ([636643a](https://github.com/KingOfKalk/icsmerger/commit/636643a09d0b2e522d5bd89dda620929b955547c))
* **deps:** Bump certifi from 2025.11.12 to 2026.1.4 ([#183](https://github.com/KingOfKalk/icsmerger/issues/183)) ([7b15f7a](https://github.com/KingOfKalk/icsmerger/commit/7b15f7ad6558ccf6b5badb798de26c6c6533ee6f))
* **deps:** Bump certifi from 2025.7.14 to 2025.8.3 ([#151](https://github.com/KingOfKalk/icsmerger/issues/151)) ([961e8b1](https://github.com/KingOfKalk/icsmerger/commit/961e8b1e4f5f8f268c03261bc37259d4c9770065))
* **deps:** Bump certifi from 2025.8.3 to 2025.10.5 ([#161](https://github.com/KingOfKalk/icsmerger/issues/161)) ([bfe44b9](https://github.com/KingOfKalk/icsmerger/commit/bfe44b9a2dba13309a7dc6ff13608c7efb48829a))
* **deps:** Bump charset-normalizer from 3.4.2 to 3.4.3 ([#152](https://github.com/KingOfKalk/icsmerger/issues/152)) ([ad4d3a1](https://github.com/KingOfKalk/icsmerger/commit/ad4d3a141c3d24756ee01e1f598305421272c6ba))
* **deps:** Bump charset-normalizer from 3.4.3 to 3.4.4 ([#167](https://github.com/KingOfKalk/icsmerger/issues/167)) ([95bc550](https://github.com/KingOfKalk/icsmerger/commit/95bc550d3bae66626f32dceab6128ede13c93b74))
* **deps:** Bump click from 8.2.1 to 8.3.0 ([#159](https://github.com/KingOfKalk/icsmerger/issues/159)) ([a6c30cc](https://github.com/KingOfKalk/icsmerger/commit/a6c30cc066655f8e81a1f423bba4afb46ff3de7c))
* **deps:** Bump click from 8.3.0 to 8.3.1 ([#175](https://github.com/KingOfKalk/icsmerger/issues/175)) ([038e997](https://github.com/KingOfKalk/icsmerger/commit/038e99753dee40d1bd4eeaafc5a01763ae0b98b2))
* **deps:** Bump github/codeql-action from 3 to 4 ([#165](https://github.com/KingOfKalk/icsmerger/issues/165)) ([28cce82](https://github.com/KingOfKalk/icsmerger/commit/28cce826f2305ec2fb3ec3f0d2fcfad808152052))
* **deps:** Bump idna from 3.10 to 3.11 ([#166](https://github.com/KingOfKalk/icsmerger/issues/166)) ([2581ad0](https://github.com/KingOfKalk/icsmerger/commit/2581ad0296cd55e257bc280ffc375646008b5b17))
* **deps:** Bump requests from 2.32.4 to 2.32.5 ([#154](https://github.com/KingOfKalk/icsmerger/issues/154)) ([1efb63e](https://github.com/KingOfKalk/icsmerger/commit/1efb63e826cf71dc7afdb5aea5d51876817b1f28))
* **deps:** Bump tatsu from 5.13.2 to 5.14.0 ([#182](https://github.com/KingOfKalk/icsmerger/issues/182)) ([2bec604](https://github.com/KingOfKalk/icsmerger/commit/2bec6044a943d513cdc16586ebc7d6b520a0cdc8))
* **deps:** Bump tatsu from 5.14.0 to 5.15.1 ([#184](https://github.com/KingOfKalk/icsmerger/issues/184)) ([6e1b35e](https://github.com/KingOfKalk/icsmerger/commit/6e1b35ea99d8e7f68ca6d286bc3daac63114d09f))
* **deps:** Bump tatsu from 5.8.3 to 5.13.2 ([#160](https://github.com/KingOfKalk/icsmerger/issues/160)) ([baad9bb](https://github.com/KingOfKalk/icsmerger/commit/baad9bbbba28c19e274bc46b488156b7793578ba))
* **deps:** Bump urllib3 from 2.5.0 to 2.6.0 ([#176](https://github.com/KingOfKalk/icsmerger/issues/176)) ([ca0c98e](https://github.com/KingOfKalk/icsmerger/commit/ca0c98e8b6526474794d5b74c84af29b48bcd60f))
* **deps:** Bump urllib3 from 2.6.0 to 2.6.1 ([#179](https://github.com/KingOfKalk/icsmerger/issues/179)) ([55aad39](https://github.com/KingOfKalk/icsmerger/commit/55aad3989f215c90a6b7f11d6f971be202b7669c))
* **deps:** Bump urllib3 from 2.6.1 to 2.6.2 ([#180](https://github.com/KingOfKalk/icsmerger/issues/180)) ([3ead522](https://github.com/KingOfKalk/icsmerger/commit/3ead522aadd944698e996581f4f3533ca507df13))
* **deps:** Bump urllib3 from 2.6.2 to 2.6.3 ([#185](https://github.com/KingOfKalk/icsmerger/issues/185)) ([17096f0](https://github.com/KingOfKalk/icsmerger/commit/17096f0598092e4904a1af2d6dd93a701ae1223e))
* **github:** [#174](https://github.com/KingOfKalk/icsmerger/issues/174): Removes deprecated CODEQL_PYTHON and setup-python-dependencies. ([#178](https://github.com/KingOfKalk/icsmerger/issues/178)) ([ba3757a](https://github.com/KingOfKalk/icsmerger/commit/ba3757a3cfde1457b5e810a9d81f7348bf378339))

## [v1.1.0] - 2025-07-18

- chore(deps): Bump urllib3 from 2.4.0 to 2.5.0 (#148)
- chore(deps-dev): Bump flake8 from 7.2.0 to 7.3.0 (#147)
- feat: Adds support for Python 3.13, removes support for Python 3.9. (#146)
- chore(deps): Bump certifi from 2025.4.26 to 2025.7.14 (#145)
- chore(deps-dev): Bump pytest from 8.3.5 to 8.4.1 (#143)
- chore(deps-dev): Bump pytest-cov from 6.1.1 to 6.2.1 (#141)
- chore(deps): Bump requests from 2.32.3 to 2.32.4 (#139)
- chore(deps): Bump click from 8.1.8 to 8.2.1 (#137)
- chore(deps): Bump charset-normalizer from 3.4.1 to 3.4.2 (#135)
- chore(deps): Bump certifi from 2025.1.31 to 2025.4.26 (#134)
- chore(deps): Bump python from 3.13.2-alpine3.20 to 3.13.3-alpine3.20 (#133)
- chore(deps): Bump urllib3 from 2.3.0 to 2.4.0 (#132)
- chore(deps-dev): Bump pytest-cov from 6.0.0 to 6.1.1 (#131)
- chore(deps-dev): Bump flake8 from 7.1.2 to 7.2.0 (#129)
- chore(deps): Bump attrs from 25.2.0 to 25.3.0 (#128)
- chore(deps): Bump attrs from 25.1.0 to 25.2.0 (#127)
- chore(deps-dev): Bump pytest from 8.3.4 to 8.3.5 (#126)
- chore(deps-dev): Bump flake8 from 7.1.1 to 7.1.2 (#125)
- chore(deps): Bump python from 3.13.1-alpine3.20 to 3.13.2-alpine3.20 (#123)
- chore(deps): Bump certifi from 2024.12.14 to 2025.1.31 (#122)
- chore(deps): Bump attrs from 24.3.0 to 25.1.0 (#121)
- chore(deps): Bump tatsu from 5.8.3 to 5.13.1 (#120)
- chore(deps): Bump charset-normalizer from 3.4.0 to 3.4.1 (#119)

**Full Changelog**: https://github.com/KingOfKalk/icsmerger/compare/v1.0.7...v1.1.0

### Important Notes

- Adds support for Python 3.13.
- Removes support for Python 3.9.

## [v1.0.7] - 2024-12-23

- Bump urllib3 from 2.2.3 to 2.3.0 (#118)
- Bump click from 8.1.7 to 8.1.8 (#117)
- Bump attrs from 24.2.0 to 24.3.0 (#116)
- Bump certifi from 2024.8.30 to 2024.12.14 (#115)
- Bump python from 3.13.0-alpine3.20 to 3.13.1-alpine3.20 (#114)
- Bump six from 1.16.0 to 1.17.0 (#113)
- Bump pytest from 8.3.3 to 8.3.4 (#112)
- Bump pytest-cov from 5.0.0 to 6.0.0 (#111)
- Bump python from 3.12.7-alpine3.20 to 3.13.0-alpine3.20 (#110)
- Bump charset-normalizer from 3.3.2 to 3.4.0 (#109)
- Bump build from 1.2.2 to 1.2.2.post1 (#108)
- Updates Python and Alpine in container. (#107)
- Bump idna from 3.8 to 3.10 (#106)
- Bump urllib3 from 2.2.2 to 2.2.3 (#105)
- Bump pytest from 8.3.2 to 8.3.3 (#104)
- Bump urllib3 from 2.2.1 to 2.2.2 (#103)
- Bump certifi from 2024.7.4 to 2024.8.30 (#102)
- Bump pytest from 8.2.2 to 8.3.2 (#101)
- Bump idna from 3.7 to 3.8 (#100)
- Bump attrs from 23.2.0 to 24.2.0 (#99)
- Bump build from 1.2.1 to 1.2.2 (#98)
- Bump flake8 from 7.1.0 to 7.1.1 (#97)

**Full Changelog**: https://github.com/KingOfKalk/icsmerger/compare/v1.0.6...v1.0.7

## [v1.0.6] - 2024-09-07

- Bump certifi from 2024.2.2 to 2024.7.4 by @dependabot in (#95)
- Bump docker/build-push-action from 5 to 6 by @dependabot in (#94)
- Bump flake8 from 7.0.0 to 7.1.0 by @dependabot in (#93)
- Bump pytest from 8.1.1 to 8.2.2 by @dependabot in (#92)
- Bump requests from 2.31.0 to 2.32.3 by @dependabot in (#90)
- Bump python from 3.12.2-alpine3.18 to 3.12.3-alpine3.18 by @dependabot in (#85)
- Bump idna from 3.6 to 3.7 by @dependabot in (#84)

**Full Changelog**: https://github.com/KingOfKalk/icsmerger/compare/v1.0.5...v1.0.6

## [v1.0.5] - 2024-04-01

- Bump build from 1.0.3 to 1.2.1 (#81)
- Bump pytest-cov from 4.1.0 to 5.0.0 (#79)
- Bump pytest from 8.0.0 to 8.1.1 (#78)
- Bump python-dateutil from 2.8.2 to 2.9.0.post0 (#77)
- Bump urllib3 from 2.2.0 to 2.2.1 (#72)
- Bump python from 3.12.1-alpine3.18 to 3.12.2-alpine3.18 (#71)
- Bump certifi from 2023.11.17 to 2024.2.2 (#70)
- Bump urllib3 from 2.1.0 to 2.2.0 (#69)
- Bump pytest from 7.4.4 to 8.0.0 (#68)
- Bump flake8 from 6.1.0 to 7.0.0 (#67)
- Bump attrs from 23.1.0 to 23.2.0 (#66)
- Bump pytest from 7.4.3 to 7.4.4 (#65)

**Full Changelog**: https://github.com/KingOfKalk/icsmerger/compare/v1.0.4...v1.0.5

## [v1.0.4] - 2023-12-22

- Bump github/codeql-action from 2 to 3. #64
- Bump actions/upload-artifact from 3 to 4. #63
- Bump actions/setup-python from 4 to 5. #62
- Bump python from 3.12.0-alpine3.18 to 3.12.1-alpine3.18. #61
- Bump idna from 3.4 to 3.6. #60
- Bump certifi from 2023.7.22 to 2023.11.17. #59
- Bump urllib3 from 2.0.7 to 2.1.0. #58
- Bump charset-normalizer from 3.3.1 to 3.3.2. #57
- Feat: Mititage TatSu's dropping of Python 3.10 support. #56
- Bump pytest from 7.4.2 to 7.4.3. #54
- Bump charset-normalizer from 3.3.0 to 3.3.1. #53
- Bump urllib3 from 2.0.6 to 2.0.7. #51

**Full Changelog**: https://github.com/KingOfKalk/icsmerger/compare/v1.0.3...v1.0.4

## [v1.0.3] - 2023-10-13

- Bumps urllib3 from 2.0.5 to 2.0.6. #48
- Adds Python 3.12 to GitHub workflows. #49
- Bumsp python from 3.11.5-alpine3.18 to 3.12.0-alpine3.18. #50

**Full Changelog**: https://github.com/KingOfKalk/icsmerger/compare/v1.0.2...v1.0.3

## [v1.0.2] - 2023-10-02

- Sets container base image to Python 3.11.4 and Alpine 3.18. #27
- Implements container based test running. #28
- Bumps charset-normalizer from 3.1.0 to 3.3.0. #25, #46
- Bumps click from 8.1.4 to 8.1.7. #26, #29, #33
- Bumps urllib3 from 2.0.3 to 2.0.5. #30, #45
- Bumps certifi from 2023.5.7 to 2023.7.22. #31
- Bumps flake8 from 6.0.0 to 6.1.0. #32
- Bumps python from 3.11.4-alpine3.18 to 3.11.5-alpine3.18. #34
- Bumps build from 0.10.0 to 1.0.3. #37
- Bumps pytest from 7.4.0 to 7.4.2. #38
- Bumps actions/checkout from 3 to 4. #39
- Bumps docker/metadata-action from 4 to 5. #40
- Bumps docker/login-action from 2 to 3. #41
- Bumps docker/build-push-action from 4 to 5. #42
- Bumps docker/setup-qemu-action from 2 to 3. #43
- Bumps docker/setup-buildx-action from 2 to 3. #44
- Bumps arrow from 1.2.3 to 1.3.0. #47

**Full Changelog**: https://github.com/KingOfKalk/icsmerger/compare/v1.0.1...v1.0.2

## [v1.0.1] - 2023-07-7

- Bumps click from 8.1.3 to 8.1.4. #23
- Bumps urllib3 from 1.26.14 to 2.0.3. #18, #20
- Bumps pytest from 7.3.1 to 7.4.0. #21, #22
- Implements GitHub Actions based Dependabot Version Updates . #17, #19

**Full Changelog**: https://github.com/KingOfKalk/icsmerger/compare/v1.0.0...v1.0.1

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

**Full Changelog**: https://github.com/KingOfKalk/icsmerger/compare/v0.0.8...v1.0.0

## [v0.0.8] - 2023-02-11

- Prepares for ics v0.9.0.
  See https://github.com/ics-py/ics-py/commit/f64c112dbacb2a49ad2ca53de8c579b5710ce992.

**Full Changelog**: https://github.com/KingOfKalk/icsmerger/compare/v0.0.7...v0.0.8

## [v0.0.7] - 2023-02-11

- Upgrades requirements and dev requirements.
- Upgrades Docker base image to python 3.11-alpine.

**Full Changelog**: https://github.com/KingOfKalk/icsmerger/compare/v0.0.6...v0.0.7

## [v0.0.6] - 2023-02-11

- Updates GitHub Action [docker-image.yml](.github/workflows/docker-image.yml) to support multi-platform builds.

**Full Changelog**: https://github.com/KingOfKalk/icsmerger/compare/v0.0.5...v0.0.6

## [v0.0.5] - 2022-02-10

- Optimized Docker image to use ENTRYPOINT and CMD better.
- Set CWD to /app/out in Docker image, so creating merged ICS files in a volume is easier.
- Updated documentation.
- Removed demo GitHub action.

**Full Changelog**: https://github.com/KingOfKalk/icsmerger/compare/v0.0.4...v0.0.5

## [v0.0.4] - 2022-02-09

- Added support for Docker.

**Full Changelog**: https://github.com/KingOfKalk/icsmerger/compare/v0.0.3...v0.0.4

## [v0.0.3] - 2021-06-15

- Implemented exception handling for HTTPS rqequests.

**Full Changelog**: https://github.com/KingOfKalk/icsmerger/compare/v0.0.2...v0.0.3

## [v0.0.2] - 2021-06-15

- Refactored project structure.
- Refactired unit tests into single files.
- Implemented option to ignore HTTP status codes equal or greater 400.

**Full Changelog**: https://github.com/KingOfKalk/icsmerger/compare/v0.0.1...v0.0.2

## [v0.0.1] - 2021-06-12

- Started project.
