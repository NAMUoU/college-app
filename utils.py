from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user
from models import ActionLog, db

def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                flash('Пожалуйста, авторизуйтесь', 'warning')
                return redirect(url_for('login'))
            
            if current_user.role not in roles:
                flash('У вас нет доступа к этой странице', 'danger')
                return redirect(url_for('dashboard'))
            
            if current_user.role == 'student':
                student_profile = current_user.student_profile
                if student_profile and student_profile.status != 'approved':
                    flash('Ваша учетная запись еще не подтверждена администратором', 'warning')
                    return redirect(url_for('dashboard'))
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def log_action(action):
    if current_user.is_authenticated:
        log = ActionLog(user_id=current_user.id, action=action)
        db.session.add(log)
        db.session.commit()

def create_notification(user_id, title, message):
    from models import Notification
    notification = Notification(user_id=user_id, title=title, message=message)
    db.session.add(notification)
    db.session.commit()