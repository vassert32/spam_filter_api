from fastapi import FastAPI
from app.models import init_db
from app.api import router

# Создаем приложение FastAPI
app = FastAPI(
    title="Spam Filter API",
    description="API для классификации сообщений на спам и не спам",
    version="1.0.0"
)

# Инициализируем БД при старте приложения
@app.on_event("startup")
def startup():
    init_db()

# Подключаем маршруты
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
