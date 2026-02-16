import os

import sentry_sdk
from dotenv import load_dotenv

load_dotenv()

def init_sentry():
    dsn = os.getenv('SENTRY_DSN')
    if not dsn:
        return
    sentry_sdk.init(
        dsn=dsn,
        send_default_pii=True,
    )
