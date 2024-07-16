#!/usr/bin/env python3
""" module for auth.py  """
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> str:
    """ Returns a salted hash of the password """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed


class Auth:
    """ Auth class """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a user in the database """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user
        else:
            raise ValueError(f'User {email} already exists')
