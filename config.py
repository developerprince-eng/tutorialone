import os
basedir = os.path.abspath(os.path.dirname(__file__))


if os.environ.get('DATABASE_URL') is None:
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'tutorial1.db')

else:
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

SECRET_KEY = 'thetutorial12019#'

CSRF_ENABLED = True

import os
basedir = os.path.abspath(os.path.dirname(__file__))


if os.environ.get('DATABASE_URL') is None:
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'tutorial1.db')

else:
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

SECRET_KEY = 'thetutorial12019#'

CSRF_ENABLED = True

