import sys
from pathlib import Path

from datetime import timedelta
from django.http import HttpResponse

sys.path.append(str(Path(__file__).resolve().parents[2]))  # корень проекта
from models.models import JwtSecret


def set_cookies(response: HttpResponse, access, refresh):
    jwt_secret = JwtSecret()
    
    response.set_cookie(
        'access_token',
        value=access,
        max_age=timedelta(days=jwt_secret.ACCESS_MAX_AGE_HOURS).total_seconds(), # Потом поменять на часы
        httponly=True,
        samesite='None',
        secure=True
        # domain=".anluck.ru", на проде, если они поддоменные api.anluck.ru и app.anluck.ru

    )
    response.set_cookie(
        'refresh_token',
        value=refresh,
        max_age=timedelta(days=jwt_secret.REFRESH_MAX_AGE_DAYS).total_seconds(),
        httponly=True,
        samesite='None',
        secure=True
        # domain=".anluck.ru", на проде, если они поддоменные api.anluck.ru и app.anluck.ru
    )
    
    return response