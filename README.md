# SWE1 Django App

[![Build Status](https://app.travis-ci.com/Ishaan-debug02/swe1-app.svg?branch=main)](https://app.travis-ci.com/github/Ishaan-debug02/swe1-app)
[![Coverage Status](https://coveralls.io/repos/github/Ishaan-debug02/swe1-app/badge.svg?branch=main)](https://coveralls.io/github/Ishaan-debug02/swe1-app?branch=main)

## CI Pipeline
- Black check
- Flake8 lint
- Django tests under coverage
- Coveralls upload
- Deploy to AWS Elastic Beanstalk on green builds

## Setup
1) Enable Travis CI for this repo at `https://app.travis-ci.com`.
2) Enable Coveralls for this repo at `https://coveralls.io`.
3) In Travis repo settings, add environment variables:
   - `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`
   - `EB_APP_NAME`, `EB_ENV_NAME`, `EB_S3_BUCKET`
4) In GitHub, enable Branch Protection: Settings → Branches → Add rule → require status checks.
5) Push a commit or open a PR to trigger CI.

## Local Development
```bash
python -m venv django-env && source django-env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## CI/CD Features Implemented ✅

- **Continuous Integration**: Travis CI runs on every push and PR
- **Code Quality**: Black formatting and Flake8 linting
- **Testing**: Automated test suite with 55% coverage
- **Coverage Tracking**: Integrated with Coveralls
- **Deployment**: Automatic deployment to AWS Elastic Beanstalk
- **Branch Protection**: Requires passing CI checks before merge
