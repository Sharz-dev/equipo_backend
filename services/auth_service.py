from models import User

def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return {"id": user.id, "email": user.email, "name": user.name}
    return None
