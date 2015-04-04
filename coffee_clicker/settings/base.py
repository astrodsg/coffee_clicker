import os 

PROJECT_DIR = os.path.realpath(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__)
            )
        )
    )

DEBUG = False

SECRET_KEY = 'sssssssshhhhh... this is a secret' # make sure to change this

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/coffee_clicker.db'

# LOGGER_NAME = ""