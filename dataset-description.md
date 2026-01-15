# 🎓 Student Dropout & Academic Success Dataset  

---

## 📌 Dataset Name
*Predict Students' Dropout and Academic Success*

---

## 🔗 Dataset Source
- *Platform:*     UCI Machine Learning Repository  
- *Donated On:*     12/12/2021  
- *Provided By:*     Higher Education Institutions (Portugal)  
- *Availability:*     Public (Research & Educational Use)

---

## 🏫 Source Introduction
This dataset originates from *Portuguese higher education institutions* and contains *real-world academic, demographic, and socio-economic data* of students. To analyze student behavior and academic performance in order to predict whether a student will:

-  *Dropout*
-  *Remain Enrolled*
-  *Graduate Successfully*

---

## ⭐ Why This Dataset Was Selected
This dataset was chosen due to the following key strengths:

-  Real-world educational data  
-  Strong *social & business impact*  
-  Ideal for *classification problems*  
-  Rich academic & behavioral features  
-  Excellent for *feature engineering & model explainability*  
-  Widely used in academic research  


---

## 📦 Dataset Size & Structure

| Attribute | Value |
|---------|------|
| Total Rows | 4,424 students |
| Total Columns | 36 features |
| Target Column | Target |
| Data Type | Mostly numerical (encoded) |
| Missing Values |  None |

---

## 🎯 Target Variable Explanation

### *Target*
Represents the final academic status of a student.

| Value | Meaning |
|------|--------|
| 0 | ❌ Dropout – student left the university |
| 1 | ⏳ Enrolled – student is still studying |
| 2 | 🎓 Graduate – student successfully completed degree |

---

## 📋 Column-Wise Description  

### 🎯 Target
Final academic status of the student.

---

### 👤 Marital Status
Marital condition of the student at enrollment.

| Value | Meaning |
|------|--------|
| 1 | Single |
| 2 | Married |
| 3 | Widower |
| 4 | Divorced |
| 5 | Facto union |
| 6 | Legally separated |

---

### 📝 Application Mode
How the student applied for university admission.

| Value | Meaning |
|------|--------|
| 1 | 1st phase – general admission |
| 2 | Ordinance No. 612/93 |
| 5 | Special access program |
| 7 | International student |
| 10 | Transfer |
| 15 | Change of course |
| 16 | Diploma holder |
| 17 | Other special regimes |

📌 Different application modes reflect *diverse academic & social backgrounds*.

---

### 🔢 Application Order
Preference order selected by the student.

| Value | Meaning |
|------|--------|
| 1 | First choice |
| 2 | Second choice |
| 3 | Third choice |
| ... | ... |

📌 *Lower value = higher preference*

---

### 🎓 Course
Encoded identifier of the academic program.

📌 Each numeric value corresponds to a specific university course  
(e.g., Engineering, Management, Education, etc.)

---

### 🕒 Daytime / Evening Attendance
Study schedule of the student.

| Value | Meaning |
|------|--------|
| 1 | Daytime classes |
| 0 | Evening classes |

---

### 📜 Previous Qualification
Highest education level before university enrollment.

| Value | Meaning |
|------|--------|
| 1 | Secondary education |
| 2 | Higher education |
| 3 | Professional course |
| 4 | Technological specialization |
| 5 | Other |

---

### 📊 Previous Qualification (Grade)
Final grade obtained in previous education.

📌 *Higher value = stronger academic background*

---

### 🌍 Nationality
Encoded nationality of the student.

| Value | Meaning |
|------|--------|
| 1 | Portuguese |
| Others | Foreign nationalities |

---

### 👩‍🎓 Mother's Qualification
Education level of the student's mother.

| Value | Meaning |
|------|--------|
| 1 | Basic education |
| 2 | Secondary education |
| 3 | Higher education |
| 4 | Master's |
| 5 | PhD |

---

### 👨‍🎓 Father's Qualification
Education level of the student's father  
📌 Uses the *same scale as mother's qualification*

---

### 👩‍💼 Mother's Occupation
Encoded job category of the student's mother.

| Value | Meaning |
|------|--------|
| 0 | Unemployed |
| 1 | Unskilled worker |
| 2 | Skilled worker |
| 3 | Professional |
| 4 | Manager |

---

### 👨‍💼 Father's Occupation
Encoded job category of the student's father  
📌 Uses the *same scale as mother's occupation*

---

### 🎂 Age at Enrollment
Age of the student at university admission (in years).

📌 *Older age may indicate a higher dropout risk*

---

### 💰 Scholarship Holder
Whether the student receives financial aid.

| Value | Meaning |
|------|--------|
| 1 | Yes |
| 0 | No |

---

### 💳 Debtor
Indicates unpaid financial obligations.

| Value | Meaning |
|------|--------|
| 1 | Yes |
| 0 | No |

---

### 🧾 Tuition Fees Up To Date
Tuition payment status.

| Value | Meaning |
|------|--------|
| 1 | Fees paid |
| 0 | Fees pending |

---

### 📚 Curricular Units – 1st Semester

- *Enrolled:* Number of subjects registered  
- *Approved:* Number of subjects passed  
- *Grade:* Average grade obtained  
- *Evaluations:* Total exams/tests attempted  

📌 Higher grades indicate better academic performance.

---

### 📚 Curricular Units – 2nd Semester

- *Enrolled:* Number of subjects registered  
- *Approved:* Number of subjects passed  
- *Grade:* Average grade obtained  
- *Evaluations:* Total exams/tests attempted  

---

### 📈 Unemployment Rate
National unemployment rate (%) during the enrollment year.

📌 Reflects *economic pressure* on students.

---

### 💹 Inflation Rate
National inflation rate (%) during the enrollment year.

---

### 🏦 GDP
Gross Domestic Product indicator of the country.

📌 Represents the *overall economic condition*.

---

## 🧠 Important Notes
- All categorical variables are *numerically encoded*
- Encoding ensures *data privacy*
-  No missing values present
-  Tree-based models can directly use the features
-  Linear models require feature scaling

---

## 🔍 Dataset Usage in This Project
This dataset is used for:

-  Exploratory Data Analysis (EDA)
-  Domain-driven Feature Engineering
-  Multiple ML model training & comparison
-  Deployment-ready ML pipeline

---

## 🏁 Final Remarks
This dataset provides a *strong foundation for predictive modeling in educational analytics*.

Its rich combination of academic, financial, and socio-economic features allows us to:
- Understand student behavior  
- Identify dropout risks early  
- Build impactful real-world Machine Learning solutions