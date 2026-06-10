from app import app, db
from models import Event, CertificateRequest

with app.app_context():
    # Добавляем колонку image_filename в Event, если её нет
    try:
        db.session.execute('ALTER TABLE events ADD COLUMN image_filename VARCHAR(200) DEFAULT "event_default.jpg"')
        print("✅ Добавлено поле image_filename в events")
    except Exception as e:
        print(f"Поле image_filename уже существует или ошибка: {e}")
    
    # Добавляем колонку certificate_type в certificate_requests
    try:
        db.session.execute('ALTER TABLE certificate_requests ADD COLUMN certificate_type VARCHAR(50) DEFAULT "study"')
        print("✅ Добавлено поле certificate_type в certificate_requests")
    except Exception as e:
        print(f"Поле certificate_type уже существует или ошибка: {e}")
    
    db.session.commit()
    print("🎉 Миграция завершена!")