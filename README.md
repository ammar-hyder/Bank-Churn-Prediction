# 🏦 Bank Customer Churn Prediction

A machine learning project to predict customer churn using classification algorithms and ensemble learning.

## 👨‍💻 Team Members

- Ammar Hyder (22K-4816)
- Muhammad Abdullah (22K-5156)
- Ausaja Hussain (22K-5186)

---

## 📄 Abstract

This project aims to develop a predictive model for identifying bank customers likely to churn. Three classification algorithms — **K-Nearest Neighbours (KNN)**, **Naive Bayes**, and **Decision Trees** — were trained and evaluated. Additionally, a **Voting Classifier** was used to ensemble these models for improved accuracy. Data visualization and exploratory data analysis (EDA) were employed to understand key patterns and features.

---

## 🧠 Introduction

Customer churn is a vital metric in the banking sector. Anticipating churn enables banks to take preemptive actions to retain customers and minimize revenue loss. This project implements machine learning algorithms to develop a model capable of predicting customer churn.

---

## 📊 Dataset & Preprocessing

- **Source**: Kaggle
- **Features**: Demographic info, account details, transaction history
- **Steps Involved**:
  - Data cleaning
  - Feature engineering
  - Class balancing (originally 80:20 → balanced to ~50:50)
  - Exploratory Data Analysis (EDA) using histograms, scatter plots, and correlation matrices

📌 *All graphs and visualizations are included in the Jupyter Notebook.*

---

## 🤖 Models Trained

1. **K-Nearest Neighbours (KNN)**
2. **Naive Bayes**
3. **Decision Trees**
4. **Voting Classifier** (Ensemble of the above models)

Each model was trained on the preprocessed data and optimized with appropriate hyperparameters.

---

## 📈 Evaluation Metrics

- **Accuracy**
- **Confusion Matrix**
- **Precision**

Visualizations were used to compare model performances.

---

## 🏁 Results

- The Voting Classifier provided the best results.
- **Accuracy**: ~80.55%
- **Precision**: ~70%
- The model performed well on the 20% test set, correctly classifying the churn status of customers.

---

## 📁 File Contents

- `Bank_Churn_Prediction.ipynb` – Main Jupyter Notebook with code, EDA, model training, and visualizations.
- `README.md` – Project overview and documentation.
- `dataset.csv` – Input dataset (if included).

---

## 📌 Conclusion

The ensemble approach using a Voting Classifier proved effective in improving predictive accuracy. This model can be used as a base for further refinement and real-time deployment in churn prediction systems.

---

