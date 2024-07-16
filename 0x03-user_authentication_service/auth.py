#!/usr/bin/env python3
""" module for auth.py  """
import bcrypt


def _hash_password(password: str) -> str:
    """ Returns a salted hash of the password """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed
