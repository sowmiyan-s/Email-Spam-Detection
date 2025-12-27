# 🛡️ Email Spam Detection System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An advanced machine learning solution designed to classify emails as **Spam** or **Ham** (Legitimate) with high precision using Support Vector Machines (SVM).

---

## 🚀 Overview

This project provides a robust end-to-end workflow for detecting fraudulent or unwanted emails. By leveraging natural language processing (NLP) and the powerful **SVM algorithm**, the system can identify sophisticated spam patterns that traditional filters might miss.

### ✨ Key Features
- **High Accuracy**: Optimized SVM model achieving over **99% accuracy**.
- **Real-time Interface**: Interactive web dashboard built with **Streamlit**.
- **Hybrid Vectorization**: Analyzes both word structures and character patterns.
- **Visual Feedback**: Dynamic animations (Snow/Balloons) and progress tracking for predictions.
- **GitHub Integrated**: Standardized styling for project documentation and repository linking.

---

## 🛠️ Tech Stack

- **Core**: Python 3.10+
- **Machine Learning**: Scikit-Learn (LinearSVC)
- **Data Engineering**: Pandas, NumPy, SciPy
- **User Interface**: Streamlit (Web App)
- **Serialization**: Joblib (for model persistence)

---

## 📂 Project Structure

```text
├── App.py                  # Main Streamlit web application
├── Final_Spam_Detector.py  # Linear workflow Python script (best for terminal)
├── spam.csv                # Cleaned dataset for training/testing
├── model.pkl               # Pre-trained SVM Model
├── vectorizer.pkl          # Multi-feature TF-IDF Vectorizer
└── README.md               # Project documentation (this file)
```

---

## ⚙️ Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Project1_Email_Spam_Detection.git
cd Project1_Email_Spam_Detection
```

### 2. Install dependencies
```bash
pip install streamlit scikit-learn pandas joblib scipy
```

### 3. Run the Applications
*   **To use the Web Dashboard:**
    ```bash
    streamlit run App.py
    ```
*   **To run via Terminal:**
    ```bash
    python Final_Spam_Detector.py
    ```

---

## 📊 Performance Analysis

| Metric | Value |
| :--- | :--- |
| **Model Type** | Linear Support Vector Machine |
| **Dataset Size** | 5,500+ Emails |
| **Final Accuracy** | **99.19%** |
| **Feature Extraction** | Word (1-3 ngrams) + Char (2-5 ngrams) + Caps Ratio |

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improving model performance or enhancing the UI, feel free to fork the repo and create a pull request.

---

## ⭐️ Support
If you find this project helpful, please give it a star on GitHub!

---
**Developed by [Sowmiyan S]**
