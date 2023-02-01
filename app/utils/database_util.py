from app.settings.configs import DATABASE_NAME, DATABASE_SERVER, DATABASE_USERNAME, DATABASE_PASSWORD

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

import urllib.parse
import sys

class database_controls(object):
    def __init__(self):
        db = sys.modules[__name__]
        self.Base = automap_base()
        password = urllib.parse.quote_plus(DATABASE_PASSWORD)
        self.quote_db = f"postgresql+psycopg2://{DATABASE_USERNAME}:{password}@{DATABASE_SERVER}:5432/{DATABASE_NAME}"

    @classmethod
    async def get_db(self):
        engine = create_engine(self.quote_db, connect_args={"timeout": 60}, pool_size=5, max_overflow=10, pool_pre_ping=True)

        SessionLocal = sessionmaker(autocommit=False, autoflush=False, expire_on_commit=True, bind=engine)
        try:
            session = SessionLocal()
            yield session
        finally:
            session.close()