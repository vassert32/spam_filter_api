from app.services.prediction import load_model, predict
from app.config import Config

# Загрузка модели
model_path = Config.MODEL_PATH
model = load_model(model_path)

# Тестовые сообщения
test_messages = [
    "Congratulations! You have won a free ticket to Bahamas.",
    "Hey, let's meet for lunch tomorrow.",
    "Limited time offer! Buy now and get 50% off.",
    "Can you send me the project report by evening?",
]

print(f"Тестирование модели по пути: {model_path}\n")

# Выполняем предсказания
for i, message in enumerate(test_messages, 1):
    prediction = predict(message, model)
    is_spam = "SPAM" if prediction else "NOT SPAM"
    print(f"Сообщение {i}: {message}")
    print(f"Предсказание: {is_spam}\n")
