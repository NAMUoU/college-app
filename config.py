import os

class Config:
    SECRET_KEY = 'dev-secret-key-change-in-production'
    
    # Используем PostgreSQL на Render, SQLite локально
    if os.environ.get('RENDER'):
        # На Render берём переменную окружения
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    else:
        # Локально — SQLite
        basedir = os.path.abspath(os.path.dirname(__file__))
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'college.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False