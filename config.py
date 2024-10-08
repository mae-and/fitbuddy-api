import os

class Config:
    SQLALCHEMY_DATABASE__URI = os.getenv('DATABASE_URL', 'postgresql://localhost/fitbuddy')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
    