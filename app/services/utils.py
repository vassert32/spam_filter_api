import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from transformers import DistilBertTokenizer, DistilBertModel
import torch
import numpy as np

# NLTK инициализация
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# Предобработка текста
def preprocess_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text).lower()
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return tokens

# Инициализация BERT
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
bert_model = DistilBertModel.from_pretrained('distilbert-base-uncased')

# Векторизация текста с использованием BERT
def vectorize_text(tokens, tokenizer=tokenizer, model=bert_model, max_length=128):
    if not tokens:
        return np.zeros(model.config.hidden_size)
    text = " ".join(tokens)
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=max_length)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
