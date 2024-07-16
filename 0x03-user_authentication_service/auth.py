#!/usr/bin/env python3
""" module for auth.py  """
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
from uuid import uuid4


def _hash_password(password: str) -> str:
    """ Returns a salted hash of the password """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed


def _generate_uuid() -> str:
    """generate a new UUID"""
    UUID = uuid4()
    return str(UUID)


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

    def valid_login(self, email: str, password: str) -> bool:
        """ checks login """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        user_password = user.hashed_password
        encoded_password = password.encode()
        if bcrypt.checkpw(encoded_password, user_password):
            return True
        return False
    
    def create_session(self, email: str) -> str:
        """ Returns new session ID """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id
