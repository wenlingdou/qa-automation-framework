from src.core.config import USER_EMAIL, USER_PASSWORD

def signin_payload():
    return {"email": USER_EMAIL, "password": USER_PASSWORD}