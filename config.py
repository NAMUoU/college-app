import os

class Config:
    SECRET_KEY = 'dev-secret-key-change-in-production'
    
    # Принудительно используем SQLite
    basedir = os.path.abspath(os.path.dirname(__file__))
    instance_path = os.path.join(basedir, 'instance')
    os.makedirs(instance_path, exist_ok=True)
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(instance_path, "college.db")}'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False