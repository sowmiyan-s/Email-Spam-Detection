from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
import pandas as pd

# 1. LOAD AND CLEAN DATA
data = pd.read_csv("spam.csv", encoding='latin-1')
df = data[['label', 'text']].dropna()



# 2. SPLIT DATA INTO TRAIN AND TEST
X_train, X_test, y_train, y_test = train_test_split(
    df['text'], 
    df['label'], 
    test_size=0.2, 
    random_state=42
)


# 3. VECTORIZATION (Standard Word-Level)
vec = TfidfVectorizer(stop_words='english', lowercase=True)
X_train_vec = vec.fit_transform(X_train)



# 4. MODEL TRAINING (Logistic Regression)
model = LogisticRegression()
model.fit(X_train_vec, y_train)



# 5. EVALUATION
y_pred = model.predict(vec.transform(X_test))
acc = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {acc * 100:.2f}%")



# 6. TESTING 
while True:
    txt = input("\nEnter Email Text :").strip()
    
    if txt:
        prediction = model.predict(vec.transform([txt]))[0]
        print(f"Result: {prediction.upper()}")
    else:
        print("Please enter some text.")
