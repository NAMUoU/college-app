from app import app, db
from models import User, StudentProfile, TeacherProfile, Group, Subject, Event, Grade, ActionLog
from datetime import datetime, date, timedelta

def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        # Создание групп
        groups = [
            Group(name='П-20-1'),
            Group(name='П-20-2'),
            Group(name='Т-20-1'),
            Group(name='Э-20-1')
        ]
        for group in groups:
            db.session.add(group)
        db.session.commit()
        
        # Создание администратора
        admin = User(
            email='admin@college.ru',
            role='admin',
            is_active=True,
            must_change_password=False
        )
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        
        # Создание преподавателя
        teacher_user = User(
            email='teacher@college.ru',
            role='teacher',
            is_active=True,
            must_change_password=True
        )
        teacher_user.set_password('teacher123')
        db.session.add(teacher_user)
        db.session.commit()
        
        teacher = TeacherProfile(
            user_id=teacher_user.id,
            full_name='Иванова Мария Петровна'
        )
        db.session.add(teacher)
        db.session.commit()
        
        # Создание дисциплин
        subjects = [
            Subject(name='Программирование', teacher_id=teacher.id),
            Subject(name='Базы данных', teacher_id=teacher.id),
            Subject(name='Web-разработка', teacher_id=teacher.id)
        ]
        for subject in subjects:
            db.session.add(subject)
        db.session.commit()
        
        # Создание студентов
        for i in range(1, 6):
            student_user = User(
                email=f'student{i}@college.ru',
                role='student',
                is_active=True,
                must_change_password=False
            )
            student_user.set_password(f'student{i}123')
            db.session.add(student_user)
            db.session.commit()
            
            student = StudentProfile(
                user_id=student_user.id,
                full_name=f'Студент {i}',
                group_id=1 if i <= 3 else 2,
                phone=f'+7(999)123-45-6{i}',
                status='approved'
            )
            db.session.add(student)
            db.session.commit()
            
            # Добавление оценок для студентов
            for subject in subjects:
                grade = Grade(
                    student_id=student.id,
                    subject_id=subject.id,
                    teacher_id=teacher.id,
                    grade_value=4 if i % 2 == 0 else 5,
                    comment='Хорошая работа',
                    grade_date=date.today() - timedelta(days=i*5)
                )
                db.session.add(grade)
            db.session.commit()
        
        # Создание мероприятий
        events = [
            Event(
                title='День открытых дверей',
                event_date=date.today() + timedelta(days=7),
                event_time='10:00',
                place='Актовый зал',
                description='Приглашаем абитуриентов и их родителей на день открытых дверей'
            ),
            Event(
                title='Хакатон по программированию',
                event_date=date.today() + timedelta(days=14),
                event_time='09:00',
                place='Компьютерный класс №301',
                description='Командное соревнование по разработке приложений'
            ),
            Event(
                title='Встреча с работодателями',
                event_date=date.today() + timedelta(days=21),
                event_time='14:00',
                place='Конференц-зал',
                description='Встреча с представителями IT-компаний'
            )
        ]
        for event in events:
            db.session.add(event)
        db.session.commit()
        
        # Создание лога
        log = ActionLog(
            user_id=admin.id,
            action='Инициализация базы данных'
        )
        db.session.add(log)
        db.session.commit()
        
        print("База данных успешно инициализирована!")
        print("\nДанные для входа:")
        print("Администратор: admin@college.ru / admin123")
        print("Преподаватель: teacher@college.ru / teacher123")
        for i in range(1, 6):
            print(f"Студент{i}: student{i}@college.ru / student{i}123")

if __name__ == '__main__':
    init_db()