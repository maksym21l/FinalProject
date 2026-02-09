import uvicorn

from app.db.database import create_db, drop_db
from app.models.buget import Budget
from app.models.users import User
from app.models.tranzactions import Tranzaction
from fastapi import FastAPI

app = FastAPI()

create_db()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)