# 🎓 Student Dropout Prediction – End-to-End Machine Learning Project

An end-to-end *Machine Learning classification project* that predicts whether a student will *Dropout, **Stay Enrolled, or **Graduate*, using real-world higher education data.  
This project covers the *complete ML lifecycle*, from raw data to deployment.

---

## 📌 Project Overview

Student dropout is a critical issue in higher education, affecting students, institutions, and society.  
This project aims to *predict student academic outcomes early*, allowing institutions to take preventive actions.

### 🎯 Problem Type
- *Multi-class Classification*
- Classes:
  - ❌ Dropout
  - 🎓 Graduate

---

## 🧠 Key Highlights

- ✔ Built *from scratch*
- ✔ Real-world educational dataset
- ✔ Strong feature engineering
- ✔ Multiple ML models compared
- ✔ Hyperparameter tuning with pipelines
- ✔ Deployment-ready architecture
- ✔ API + Frontend + Dockerized

---

## 📂 Dataset Information

- *Source:* UCI Machine Learning Repository  
- *Initial Features:* 37  
- *Final Features Used:* 18  
- *Target Variable:* Target  
- *Missing Values:*  None  

📌 A *detailed dataset description* is available in:  
👉 DATASET_DESCRIPTION.md

---

## 🧹 Data Cleaning & Feature Engineering

### 🔹 Raw Dataset
- Contained *37 features*
- Many features were:
  - Not always available
  - Redundant
  - Weakly correlated with the target

### 🔹 Feature Engineering Strategy
- Removed low-impact and rarely available features
- Merged related academic attributes
- Retained only *highly informative & practical features*
- Final dataset reduced to *18 strong features*

📌 Result:
> *Cleaner data + better generalization + realistic deployment*

---

## 🔍 Exploratory Data Analysis (EDA)

Performed deep EDA to understand:
- Dropout patterns
- Academic performance trends
- Financial & socio-economic impact
- Feature importance signals

### 📊 Visual Analysis Included
- Target class distribution
- Correlation heatmaps
- Feature-wise comparisons
- Performance-based insights

---

## ⚙️ Machine Learning Pipeline

### 🔹 Models Trained
The following *4 classification models* were trained and evaluated:

| Model | Description |
|-----|------------|
| Logistic Regression | Baseline linear model |
| Random Forest | Tree-based ensemble |
| Support Vector Machine (SVM) | Margin-based classifier |
| XGBoost | Gradient boosting model |

---

## 🧪 Hyperparameter Tuning

- Created *separate pipelines* for each model
- Used *hyperparameter tuning* to optimize performance
- Ensured fair and consistent comparison

📌 All models were trained on the *same processed dataset*

---

## 📈 Model Evaluation & Comparison

### 🔹 Metrics Used
- Accuracy
- Precision
- Recall
- F1-score

### 🔹 Visualization
- 📊 Accuracy comparison charts
- 📊 Precision comparison charts

---

## 📊 Model Training & Evaluation

I compared four different machine learning models and developed Hyperparameter Tuning Pipelines for each to ensure optimal performance::

| Model | Accuracy | Precision | Status |
| :--- | :---: | :---: | :--- |
| **Logistic Regression** | 85% | 84% | Baseline |
| **Random Forest** | 88% | 87% | Strong Competitor |
| **SVM** | 84% | 83% | Robust |
| **XGBoost 🏆** | **90%** | **89%** | **Final Selected Model** |

### 📈 Why XGBoost?
XGBoost delivered the best performance with an accuracy of 90%. It excels at capturing complex non-linear relationships within the data while effectively controlling for overfitting. Furthermore, its high precision is crucial for accurately identifying students at risk of dropping out, minimizing false alarms.

### ✅ *Final Selected Model*
| Model | Accuracy |
|-----|----------|
| *XGBoost* | *90%* |

📌 *Why XGBoost?*
- Highest accuracy
- Better generalization
- Strong handling of feature interactions
- Best fit for this problem

---

## 💾 Model Saving

- Saved:
  - Trained models
  - Test datasets
- Ensured reproducibility
- Ready for deployment & inference

---

## 🚀 API Development (FastAPI)

- Built a *REST API* using *FastAPI*
- Handles:
  - Input validation
  - Model inference
  - JSON-based responses

📌 API allows external systems to use the model independently.

---

## 🖥️ Frontend (Streamlit)

- Developed a *simple & clean frontend*
- Users can:
  - Enter student details
  - Get real-time predictions
- Designed for *demo & usability*

---

## 🐳 Dockerization

- Created a *Dockerfile*
- Entire application is:
  - Portable
  - Environment-independent
  - Easy to deploy

📌 Ensures consistency across systems.

---

## 🛠️ Tech Stack
* **Backend:** FastAPI (Python)
* **Frontend:** Streamlit
* **Machine Learning:** XGBoost, Scikit-Learn, Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Deployment:** Docker
* **Model Saving:** Joblib

---

## 🧩 Project Architecture

```text
📂 STUDENT-DROPOUT-RISK-PREDICTION/
│
├── 📂 api/
│   └── 📄 main.py
│
├── 📂 data/
│   ├── 📄 raw-data.csv
│   ├── 📄 cleaned-data.csv
│   └── 📄 featured-data.csv
│
├── 📂 frontend/
│   └── 📄 app.py
│
├── 📂 models & test data/
│   ├── 📂 logistic-regression/
│   │   ├── 📄 logistic-regression-model.pkl
│   │   ├── 📄 logistic-regression-X_test.pkl
│   │   └── 📄 logistic-regression-y_test.pkl
│   │
│   ├── 📂 random-forest/
│   │   ├── 📄 random-forest-model.pkl
│   │   ├── 📄 random-forest-X_test.pkl
│   │   └── 📄 random-forest-y_test.pkl
│   │
│   ├── 📂 svm/
│   │   ├── 📄 svm-model.pkl
│   │   ├── 📄 svm-X_test.pkl
│   │   └── 📄 svm-y_test.pkl
│   │
│   └── 📂 xgboost/
│       ├── 📄 xgboost-model.pkl
│       ├── 📄 xgboost-X_test.pkl
│       └── 📄 xgboost-y_test.pkl
│
├── 📂 notebooks/
│   ├── 📂 Automated-EDA Results/
│   ├── 📂 AutoViz_Plots/
│   ├── 📄 Pandas_Profiling.html
│   │
│   ├── 📂 EDA/
│   │   ├── 📄 automated-EDA.ipynb
│   │   └── 📄 manual-EDA.ipynb
│   │
│   └── 📂 Model Training/
│       ├── 📄 logistic-regression.ipynb
│       ├── 📄 random-forest.ipynb
│       ├── 📄 SVM.ipynb
│       ├── 📄 XGBoost.ipynb
│       ├── 📄 data-cleaning.ipynb
│       ├── 📄 feature-engineering.ipynb
│       └── 📄 models-evaluation-comparison.ipynb
│
├── 📄 dataset-description.md
└── 📄 README.md
