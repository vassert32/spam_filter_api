import joblib
from app.services.utils import preprocess_text, vectorize_text

# Загрузка модели
def load_model(model_path='models/spam_classifier_rf.pkl'):
    return joblib.load(model_path)

# Предсказание
def predict(text, model):
    tokens = preprocess_text(text)
    vector = vectorize_text(tokens)
    prediction = model.predict([vector])[0]
    return prediction
