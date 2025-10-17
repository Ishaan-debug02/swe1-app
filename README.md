# SWE1 Django App

[![Build Status](https://app.travis-ci.com/Ishaan-debug02/swe1-app.svg?branch=main)](https://app.travis-ci.com/github/Ishaan-debug02/swe1-app)
[![Coverage Status](https://coveralls.io/repos/github/Ishaan-debug02/swe1-app/badge.svg?branch=main)](https://coveralls.io/github/Ishaan-debug02/swe1-app?branch=main)

Replace `USER` with your GitHub username.

## CI Pipeline
- Black check
- Flake8 lint
- Django tests under coverage
- Coveralls upload
- Deploy to AWS Elastic Beanstalk on green builds

## Setup
1) Replace `USER` above with your GitHub username and commit.
2) Enable Travis CI for this repo at `https://app.travis-ci.com`.
3) Enable Coveralls for this repo at `https://coveralls.io`.
4) In Travis repo settings, add environment variables:
   - `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`
   - `EB_APP_NAME`, `EB_ENV_NAME`, `EB_S3_BUCKET`
   - If private repo, also set `COVERALLS_REPO_TOKEN`
5) In GitHub, enable Branch Protection: Settings → Branches → Add rule → require status checks.
6) Push a commit or open a PR to trigger CI.

## Local Development
```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


Testing Travis CI integration

## CI/CD Pipeline Active
# Testing AWS deployment
# Coveralls enabled
