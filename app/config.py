import os

# Конфигурация приложения
class Config:
    # Путь к данным
    DATA_PATH = os.getenv("DATA_PATH", "./app/data/spam.csv")  # Учитывает путь в Docker-контейнере
    MODEL_PATH = os.getenv("MODEL_PATH", "./app/models/spam_classifier_rf.pkl")  # Путь к модели в Docker-контейнере

    # URL базы данных
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@db:5432/spam_filter"
    )  # Подключение к PostgreSQL, учитывая Docker Compose
