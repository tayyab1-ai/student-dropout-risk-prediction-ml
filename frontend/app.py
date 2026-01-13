import streamlit as st
import requests
import subprocess
import sys
import os

# Page Config
st.set_page_config(
    page_title="EduPredict | Dropout Risk Dashboard",
    page_icon="🎓",
    layout="wide"
)

# Advanced Professional Styling
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #f4f7f9;
    }
    /* Custom Card Style */
    .input-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #007bff;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    /* Button Hover */
    .stButton>button {
        background-image: linear-gradient(to right, #007bff, #0056b3);
        color: white;
        border: none;
        transition: 0.3s;
        font-size: 18px;
        height: 3.5rem;
    }
    .stButton>button:hover {
        opacity: 0.9;
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for Guidance and Info
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3413/3413535.png", width=100)
    st.title("System Guide")
    st.info("""
    **Ranges Info:**
    - **Grades:** 0 to 20 scale.
    - **Qualification Grades:** 0 to 200 scale.
    - **Codes:** Use institutional standard codes.
    """)
    st.warning("⚠️ Ensure all semester data is accurate for better prediction.")

# Header Section
col_t1, col_t2 = st.columns([1, 4])
with col_t1:
    st.write("") 
with col_t2:
    st.title("🎓 Student Success & Risk Analytics")
    st.markdown("Predict academic outcomes using machine learning and historical data.")

# Form & Layout
API_URL = "http://127.0.0.1:8000/predict"

with st.container():
    with st.form("main_form"):
        # Top Row: Personal Details
        st.markdown("### 👤 Section 1: Demographic Profile")
        c1, c2, c3 = st.columns(3)
        with c1:
            gender = st.selectbox("Gender", [(1, "Male"), (0, "Female")], format_func=lambda x: x[1])[0]
            age_at_enrollment = st.number_input("Enrollment Age", 15, 100, 20)
        with c2:
            marital_status = st.selectbox("Marital Status", [(1, "Single"), (2, "Married"), (3, "Widower"), (4, "Divorced")], format_func=lambda x: x[1])[0]
            attendance = st.selectbox("Attendance", [(1, "Daytime"), (0, "Evening")], format_func=lambda x: x[1])[0]
        with c3:
            is_displaced = st.selectbox("Is Displaced?", [(1, "Yes"), (0, "No")], format_func=lambda x: x[1])[0]
            special_needs = st.selectbox("Special Needs?", [(1, "Yes"), (0, "No")], format_func=lambda x: x[1])[0]

        st.divider()

        # Middle Row: Finance & Background
        st.markdown("### 💵 Section 2: Financial & Academic Background")
        c4, c5, c6 = st.columns(3)
        with c4:
            is_debtor = st.selectbox("Has Unpaid Debt?", [(1, "Yes"), (0, "No")], format_func=lambda x: x[1])[0]
            scholarship = st.selectbox("Scholarship Holder?", [(1, "Yes"), (0, "No")], format_func=lambda x: x[1])[0]
        with c5:
            tuition_fees = st.selectbox("Tuition Fees Up to Date?", [(1, "Yes"), (0, "No")], format_func=lambda x: x[1])[0]
            prev_qual = st.number_input("Prev. Qualification Code", value=1)
        with c6:
            prev_grade = st.number_input("Prev. Qual. Grade (0-200)", 0.0, 200.0, 120.0)
            adm_grade = st.number_input("Admission Grade (0-200)", 0.0, 200.0, 120.0)

        st.divider()

        # Bottom Row: Performance
        st.markdown("### 📈 Section 3: Academic Performance (Semester Wise)")
        c7, c8 = st.columns(2)
        with c7:
            with st.expander("1st Semester Details", expanded=True):
                c1_app = st.number_input("Approved Units (Sem 1)", 0, 30, 5)
                c1_grade = st.number_input("Average Grade (Sem 1)", 0.0, 20.0, 12.0)
        with c8:
            with st.expander("2nd Semester Details", expanded=True):
                c2_app = st.number_input("Approved Units (Sem 2)", 0, 30, 5)
                c2_grade = st.number_input("Average Grade (Sem 2)", 0.0, 20.0, 12.0)
                c2_eval = st.number_input("Units Without Eval (Sem 2)", 0, 10, 0)

        # Center Submit Button
        st.write("")
        submit = st.form_submit_button("GENERATE ANALYTICS REPORT")

# Results Logic
if submit:
    payload = {
        "marital_status": marital_status,
        "daytime_evening_attendance": attendance,
        "previous_qualification": prev_qual,
        "previous_qualification_grade": prev_grade,
        "admission_grade": adm_grade,
        "is_displaced": is_displaced,
        "educational_special_needs": special_needs,
        "is_debtor": is_debtor,
        "tuition_fees_up_to_date": tuition_fees,
        "gender": gender,
        "is_scholarship_holder": scholarship,
        "age_at_enrollment": age_at_enrollment,
        "curricular_units_1st_sem_approved": c1_app,
        "curricular_units_1st_sem_grade": c1_grade,
        "curricular_units_2nd_sem_approved": c2_app,
        "curricular_units_2nd_sem_grade": c2_grade,
        "curricular_units_2nd_sem_without_evaluations": c2_eval
    }

    try:
        with st.spinner('Running AI Analysis...'):
            response = requests.post(API_URL, json=payload)
            result = response.json()
        
        # UI for Result
        st.markdown("---")
        res_col1, res_col2 = st.columns([1, 1])
        
        with res_col1:
            if result["prediction"] == "Graduate":
                st.balloons()
                st.success(f"### Prediction: {result['prediction']}")
            else:
                st.error(f"### Prediction: {result['prediction']}")
            
            st.write(f"The model is **{result['probability']*100}%** certain about this outcome.")

        with res_col2:
            # Probability Gauge
            st.write("Confidence Level")
            st.progress(result['probability'])
            
    except Exception as e:
        st.error("Connection Error: Could not reach the API. Please ensure FastAPI is active.")

# Self-execution logic
if __name__ == "__main__":
    if not os.environ.get("STREAMLIT_RUNNING"):
        os.environ["STREAMLIT_RUNNING"] = "True"
        try:
            subprocess.run([sys.executable, "-m", "streamlit", "run", __file__])
        except Exception:
            pass