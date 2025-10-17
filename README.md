# SWE1 Django App

[![Build Status](https://app.travis-ci.com/Ishaan-debug02/swe1-app.svg?branch=main)](https://app.travis-ci.com/github/Ishaan-debug02/swe1-app)
[![Coverage Status](https://coveralls.io/repos/github/Ishaan-debug02/swe1-app/badge.svg)](https://coveralls.io/github/Ishaan-debug02/swe1-app)

## CI/CD Pipeline Status

- ✅ **Build**: Passing (Travis CI)
- ✅ **Coverage**: 54.95% (Coveralls)
- ✅ **Code Quality**: Black + Flake8 passing
- ✅ **Tests**: 4/4 tests passing
- ✅ **Deployment**: AWS Elastic Beanstalk

## Features Implemented

- **Continuous Integration**: Travis CI runs on every push and PR
- **Code Quality**: Black formatting and Flake8 linting enforced
- **Testing**: Automated test suite with coverage reporting
- **Coverage Tracking**: Real-time coverage via Coveralls (54.95%)
- **Deployment**: Automatic deployment to AWS EB on green builds
- **Branch Protection**: CI checks required before merge

## Project Links

- **Travis CI Dashboard**: https://app.travis-ci.com/github/Ishaan-debug02/swe1-app
- **Coveralls Coverage**: https://coveralls.io/github/Ishaan-debug02/swe1-app
- **Live Application**: http://swe1-app-dev.us-east-1.elasticbeanstalk.com/polls/
- **GitHub Repository**: https://github.com/Ishaan-debug02/swe1-app

## Local Development
```bash
python -m venv django-env && source django-env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Running Tests Locally
```bash
black --check .
flake8 .
python manage.py test
coverage run --source='.' manage.py test
coverage report
```

## Assignment Completion ✅

This project demonstrates a complete CI/CD pipeline with:
- Automated testing on every commit
- Code quality enforcement
- Coverage tracking
- Automated deployment
- Branch protection requiring green builds
