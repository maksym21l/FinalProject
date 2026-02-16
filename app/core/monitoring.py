import os

import sentry_sdk
from dotenv import load_dotenv

from app.utils.error_handler import AppError

load_dotenv()

def init_sentry():
    dsn = os.getenv('SENTRY_DSN')
    if not dsn:
        return
    sentry_sdk.init(
        dsn=dsn,
        send_default_pii=True,
    )



def fail_monitor(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except AppError as e:
            sentry_sdk.capture_exception(f"CRITICAL!!! {e}")
            return None
    return wrapper