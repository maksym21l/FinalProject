from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQL_DB_URL = 'sqlite:///./fast_api.db'

engine = create_engine(
    SQL_DB_URL,
    connect_args={'check_same_thread': False}
)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # Виправлено autocommit

Base = declarative_base()

# Функція для отримання сесії БД
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


def create_db():
    Base.metadata.create_all(bind=engine)

def drop_db():
    Base.metadata.drop_all(bind=engine)
