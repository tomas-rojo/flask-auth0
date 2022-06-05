from flask_login import UserMixin

from db import get_db
from test import get_user, add_new_user

class User(UserMixin):
    def __init__(self, id_, name, email, profile_pic):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic

    @staticmethod
    def get(user_id):
        # db = get_db()
        # user = db.execute(
        #     "SELECT * FROM user WHERE id = ?", (user_id,)
        # ).fetchone()
        user = get_user(user_id)
        if not user:
            return None

        user = User( 
            id_=user[0], name=user[1], email=user[2], profile_pic=user[3]
        )
        return user

    @staticmethod
    def create(id_, name, email, profile_pic):
        add_new_user(id_, name, email, profile_pic)
