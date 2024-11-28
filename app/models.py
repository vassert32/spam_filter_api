from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import Config

# Настройка БД
Base = declarative_base()
engine = create_engine(Config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Модель для хранения запросов
class SpamRequest(Base):
    __tablename__ = "spam_requests"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    is_spam = Column(Boolean, nullable=False)

# Инициализация БД
def init_db():
    Base.metadata.create_all(bind=engine)
