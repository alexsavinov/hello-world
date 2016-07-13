# -*- coding: utf-8 -*-
"""Configuration module."""

CSRF_ENABLED = True
SECRET_KEY = 'n1DsjfhLKHf88dfdHFljdshflk0d'
DEBUG = True
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
BABEL_DEFAULT_LOCALE = 'ru'
BABEL_DEFAULT_TIMEZONE = 'UTC'
LANGUAGES = {
    'en': 'English',
    'ru': 'Русский'
}