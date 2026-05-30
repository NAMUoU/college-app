from app import app, db
from models import User, StudentProfile, TeacherProfile, Group, Subject, Event

def init_database():
    with app.app_context():
        print("🗄️ Создание таблиц базы данных...")
        db.create_all()
        print("✅ Таблицы созданы")
        
        # Проверяем, есть ли данные
        if User.query.count() == 0:
            print("📦 База данных пуста. Заполняем тестовыми данными...")
            
            # Создаём администратора
            admin = User(
                email='admin@college.ru',
                role='admin',
                is_active=True,
                must_change_password=False
            )
            admin.set_password('admin123')
            db.session.add(admin)
            
            # Создаём группы
            groups = [
                Group(name='П-20-1'),
                Group(name='П-20-2'),
                Group(name='Т-20-1'),
            ]
            for group in groups:
                db.session.add(group)
            
            db.session.commit()
            print("✅ Тестовые данные добавлены")
        else:
            print("✅ Данные уже есть в базе")

if __name__ == '__main__':
    init_database()
    print("🎉 Инициализация завершена!")