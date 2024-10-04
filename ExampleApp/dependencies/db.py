
from databases import SessionLocal
from sqlalchemy.orm import Session



def get_db() -> Session:
    """
    获取db session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



