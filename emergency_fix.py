from app import app, db
from models import User

with app.app_context():
    # Удаляем всех пользователей
    User.query.delete()
    db.session.commit()
    
    # Создаём админа заново
    admin = User(
        email='admin@college.ru',
        role='admin',
        is_active=True,
        must_change_password=False
    )
    admin.set_password('admin123')
    db.session.add(admin)
    db.session.commit()
    
    print("✅ Администратор создан заново!")
    print("📧 Email: admin@college.ru")
    print("🔑 Пароль: admin123")
    
    # Проверяем
    test = User.query.filter_by(email='admin@college.ru').first()
    if test and test.check_password('admin123'):
        print("✅ Проверка пройдена: можно входить!")
    else:
        print("❌ Ошибка: что-то не так с хешированием")