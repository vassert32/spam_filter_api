import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from app.services.utils import preprocess_text, vectorize_text # utils.py

# Обучение модели
def train_model(data_path, model_save_path='models/spam_classifier_rf.pkl'):
    # Проверяем загрузку данных
    df = pd.read_csv(data_path, encoding='latin1')
    print(f"Размер загруженного датасета: {df.shape}")

    # Удаляем лишние столбцы, если они есть
    df = df.rename(columns={"v1": "target", "v2": "text"})
    df = df[['text', 'target']]  # Оставляем только нужные столбцы

    # Удаляем дубликаты
    df = df.drop_duplicates(subset='text')

    df['target'] = df['target'].map({'ham': 0, 'spam': 1})

    # Предобработка текста
    df['lemm_text'] = df['text'].apply(preprocess_text)

    # Векторизация
    X = np.array([vectorize_text(tokens) for tokens in df['lemm_text']])
    y = df['target']

    analyze_vectors(X)

    # Разделение на тренировочные и тестовые данные
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Обучение модели
    model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train, y_train)

    from sklearn.metrics import classification_report

    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Сохранение модели
    joblib.dump(model, model_save_path)
    print(f"Модель сохранена по пути: {model_save_path}")
    return model

def analyze_vectors(X):
    print(f"Размерность матрицы признаков: {X.shape}")
    # print(f"Пример первого вектора: {X[0]}")
    print(f"Среднее значение по каждому признаку (основные 10): {X.mean(axis=0)[:10]}")
    print(f"Сумма всех значений вектора для первой строки: {X[0].sum()}")
