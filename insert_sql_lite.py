from extensions import db
from models import User
from werkzeug.security import generate_password_hash

def add_user(email, password):
    user = User(email=email, password_hash=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()

if __name__ == "__main__":
    from app import create_app
    app = create_app()
    with app.app_context():
        add_user("Test@gmail.com", "Password")
