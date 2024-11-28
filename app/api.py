from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.services.prediction import load_model, predict
from app.models import SpamRequest, SessionLocal
from app.config import Config
from pydantic import BaseModel

# Загрузка модели
model = load_model(Config.MODEL_PATH)

# Инициализация роутера
router = APIRouter()

# Сессия для работы с БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Схема для входных данных
class MessageRequest(BaseModel):
    message: str

# Схема для выходных данных
class MessageResponse(BaseModel):
    id: int
    message: str
    is_spam: bool

# Эндпоинт для предсказания
@router.post("/predict/", response_model=dict, summary="Предсказать, является ли сообщение спамом")
async def predict_message(request: MessageRequest, db: Session = Depends(get_db)):
    if not request.message:
        raise HTTPException(status_code=400, detail="Сообщение не может быть пустым")

    # Выполняем предсказание
    is_spam = bool(predict(request.message, model))

    # Сохраняем запрос в БД
    spam_request = SpamRequest(message=request.message, is_spam=is_spam)
    db.add(spam_request)
    db.commit()
    db.refresh(spam_request)

    return {"message": request.message, "is_spam": is_spam}

# Эндпоинт для получения всех запросов
@router.get("/requests/", response_model=list[MessageResponse], summary="Получить историю запросов")
async def get_requests(db: Session = Depends(get_db)):
    requests = db.query(SpamRequest).all()
    return [{"id": r.id, "message": r.message, "is_spam": r.is_spam} for r in requests]
