from app.services.training import train_model
from app.services.prediction import predict
from app.config import Config

import nltk
import os
nltk.download('stopwords')
nltk.download('wordnet')
nltk.data.path.append(os.path.expanduser("~/nltk_data"))
nltk.download('punkt')
nltk.download('punkt_tab')


# Указываем путь до данных
data_path = Config.DATA_PATH

# Обучение модели
if __name__ == "__main__":
    print("Начало обучения модели...")
    train_model(data_path, Config.MODEL_PATH)
    print(f"Модель сохранена по пути: {Config.MODEL_PATH}")
