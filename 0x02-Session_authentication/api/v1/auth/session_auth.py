#!/usr/bin/env python3
"""Session Authentication"""
from api.v1.auth.auth import Auth
from typing import Dict
import uuid


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
