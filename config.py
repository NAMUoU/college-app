import os
from pathlib import Path

class Config:
    SECRET_KEY = 'dev-secret-key-change-in-production'
    
    # Получаем абсолютный путь к папке проекта
    basedir = Path(__file__).resolve().parent
    
    # Создаём папку instance (где будет лежать БД)
    instance_path = basedir / 'instance'
    instance_path.mkdir(exist_ok=True)
    
    # Правильный путь к SQLite базе данных
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{instance_path}/college.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False