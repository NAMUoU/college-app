import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Получаем строку подключения из переменных окружения
    database_url = os.environ.get('DATABASE_URL')
    
    if database_url:
        # На Render с PostgreSQL
        # Исправляем формат: postgres:// → postgresql://
        if database_url.startswith('postgres://'):
            database_url = database_url.replace('postgres://', 'postgresql://', 1)
        SQLALCHEMY_DATABASE_URI = database_url
        print(f"✅ Используется PostgreSQL: {database_url[:50]}...")
    else:
        # Локальная разработка с SQLite
        basedir = os.path.abspath(os.path.dirname(__file__))
        instance_path = os.path.join(basedir, 'instance')
        os.makedirs(instance_path, exist_ok=True)
        SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(instance_path, "college.db")}'
        print("✅ Используется SQLite (локально)")
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False