from sqlalchemy import create_engine
from db.config import PG_PATH

engine = create_engine(
    PG_PATH, echo=True)
