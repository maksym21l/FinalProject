from fastapi import FastAPI

from app.repositories.users import get_user_by_id_or_error
from app.core.monitoring import fail_monitor

app = FastAPI()

@fail_monitor
@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    return get_user_by_id_or_error(user_id=user_id)


