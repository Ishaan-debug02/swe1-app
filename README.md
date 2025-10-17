# SWE1 Django App

![Build Status](https://img.shields.io/travis/com/Ishaan-debug02/swe1-app/main?label=build)
![Coverage](https://img.shields.io/coveralls/github/Ishaan-debug02/swe1-app/main?label=coverage)

## CI/CD Status Dashboard

**Current Status:** All checks passing ✅

| Component | Status | Details |
|-----------|--------|---------|
| **Build** | ![passing](https://img.shields.io/badge/build-passing-brightgreen) | Travis CI automated builds |
| **Tests** | ![4/4](https://img.shields.io/badge/tests-4%2F4%20passing-brightgreen) | All unit tests passing |
| **Coverage** | ![54.95%](https://img.shields.io/badge/coverage-54.95%25-yellow) | Code coverage tracked |
| **Linting** | ![passing](https://img.shields.io/badge/black-passing-brightgreen) ![passing](https://img.shields.io/badge/flake8-passing-brightgreen) | Code quality checks |
| **Deployment** | ![deployed](https://img.shields.io/badge/AWS%20EB-deployed-blue) | Live on Elastic Beanstalk |

## Quick Links

- 🔨 [Travis CI Dashboard](https://app.travis-ci.com/github/Ishaan-debug02/swe1-app) - View build history
- 📊 [Coveralls Report](https://coveralls.io/github/Ishaan-debug02/swe1-app) - View coverage details
- 🚀 [Live Application](http://swe1-app-dev.us-east-1.elasticbeanstalk.com/polls/) - Deployed app
- 📁 [GitHub Repository](https://github.com/Ishaan-debug02/swe1-app) - Source code

## CI/CD Pipeline

This project implements a complete CI/CD pipeline with:

### Automated Checks ✅
- **Black**: Code formatting validation
- **Flake8**: Linting and style checking  
- **Tests**: Full test suite execution
- **Coverage**: Code coverage analysis (54.95%)

### Integration Services
- **Travis CI**: Continuous Integration platform
- **Coveralls**: Coverage tracking and reporting
- **AWS Elastic Beanstalk**: Automated deployment

### Branch Protection 🔒
- Requires passing CI checks before merge
- Enforces code quality standards
- Prevents breaking changes

## Local Development
```bash
# Setup virtual environment
python -m venv django-env && source django-env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

## Running Tests
```bash
# Format code
black .

# Check linting
flake8 .

# Run test suite
python manage.py test

# Generate coverage report
coverage run --source='.' manage.py test
coverage report
```

## Deployment

The application automatically deploys to AWS Elastic Beanstalk when:
- All CI checks pass ✅
- Changes are pushed to `main` branch
- Build completes successfully

**Live URL**: http://swe1-app-dev.us-east-1.elasticbeanstalk.com/polls/

## Project Structure
```
swe1-app/
├── .travis.yml          # CI/CD configuration
├── mysite/              # Django project settings
├── polls/               # Main application
│   ├── models.py
│   ├── views.py
│   ├── tests.py
│   └── templates/
├── requirements.txt     # Python dependencies
└── README.md
```

## Assignment Requirements Met

✅ Travis CI configured for automatic builds  
✅ Black code formatting check  
✅ Flake8 linting  
✅ Test suite with coverage  
✅ Coveralls integration  
✅ AWS Elastic Beanstalk deployment  
✅ Branch protection enabled  
✅ Build/coverage badges displayed  
