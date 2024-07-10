#!/usr/bin/env python3
"""Session Authentication"""
from api.v1.auth.auth import Auth
from typing import Dict
import uuid
from models.user import User


class SessionAuth(Auth):
    """ Session class inherits Auth """
    user_id_by_session_id: Dict[str, str] = {}

    def create_session(self, user_id: str = None) -> str:
        """ Session ID creator """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_ids

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns session id based on user id """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None):
        """ Returns User cookie value """
        cookie = self.session_cookie(request)
        session_user_id = self.user_id_for_session_id(cookie)
        user_id = User.get(session_user_id)
        return user_id

