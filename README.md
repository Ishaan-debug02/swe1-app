# SWE1 Django App

## CI/CD Status

| Check | Status | Link |
|-------|--------|------|
| **Build** | ✅ Passing | [View on Travis CI](https://app.travis-ci.com/github/Ishaan-debug02/swe1-app) |
| **Coverage** | ✅ 54.95% | [View on Coveralls](https://coveralls.io/github/Ishaan-debug02/swe1-app) |
| **Deployment** | ✅ Live | [View Application](http://swe1-app-dev.us-east-1.elasticbeanstalk.com/polls/) |

[![Build Status](https://app.travis-ci.com/Ishaan-debug02/swe1-app.svg?branch=main)](https://app.travis-ci.com/github/Ishaan-debug02/swe1-app)
[![Coverage Status](https://coveralls.io/repos/github/Ishaan-debug02/swe1-app/badge.svg)](https://coveralls.io/github/Ishaan-debug02/swe1-app)

## CI/CD Pipeline Features

- ✅ **Black Code Formatting**: Automated style checking
- ✅ **Flake8 Linting**: Code quality enforcement
- ✅ **Automated Testing**: 4/4 tests passing
- ✅ **Coverage Reporting**: 54.95% code coverage tracked
- ✅ **Coveralls Integration**: Real-time coverage monitoring
- ✅ **AWS Deployment**: Automatic deployment to Elastic Beanstalk
- ✅ **Branch Protection**: Requires passing CI before merge

## Project Links

- **Travis CI Dashboard**: https://app.travis-ci.com/github/Ishaan-debug02/swe1-app
- **Coveralls Coverage Report**: https://coveralls.io/github/Ishaan-debug02/swe1-app
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
# Format code
black .

# Check linting
flake8 .

# Run tests
python manage.py test

# Generate coverage report
coverage run --source='.' manage.py test
coverage report
```

## CI/CD Workflow

1. Developer pushes code or opens PR
2. Travis CI automatically runs:
   - Black formatting check
   - Flake8 linting
   - Full test suite
   - Coverage analysis
3. Coverage report uploaded to Coveralls
4. On success, deploys to AWS Elastic Beanstalk
5. Branch protection prevents merging failed builds
