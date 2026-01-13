from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import uvicorn


# initialize FastAPI app
app = FastAPI(
    title="Student Dropout Risk Prediction API",
    description="Predicts student academic outcome using XGBoost",
    version="1.0"
)


# load XGBoost Model
MODEL_PATH = "models & test data/xgboost/xgboost-model.pkl"
model = joblib.load(MODEL_PATH)


# define input features
# features used by the XGBoost model (17 features)
class StudentInput(BaseModel):
    # Demographics
    marital_status: int                                   # 1: Single, 2: Married, 3: Widower, 4: Divorced, 5: Facto Union, 6: Legally Separated
    daytime_evening_attendance: int                       # 1: Daytime (Classes during the day), 0: Evening (Classes at night)
    
    # Academic History
    previous_qualification: int                           # Education level ID (e.g., 1: Secondary Education, 2: Higher Education Degree)
    previous_qualification_grade: float                   # Grade from previous education (Scale: 0 to 200)
    admission_grade: float                                # Grade obtained in the university entrance exam (Scale: 0 to 200)
    
    # Personal Situation
    is_displaced: int                                     # 1: Yes (Living away from home), 0: No
    educational_special_needs: int                        # 1: Yes (Requires special educational support), 0: No
    is_debtor: int                                        # 1: Yes (Student has outstanding debt/fees), 0: No
    tuition_fees_up_to_date: int                          # 1: Yes (Fees are paid), 0: No
    gender: int                                           # 1: Male, 0: Female
    is_scholarship_holder: int                            # 1: Yes (Receiving financial aid), 0: No
    age_at_enrollment: int                                # Student's age at the time of joining (e.g., 18, 22, 35)
    
    # Academic Performance - 1st Semester
    curricular_units_1st_sem_approved: int                # Number of subjects passed in the 1st semester
    curricular_units_1st_sem_grade: float                 # Average grade in 1st semester (Scale: 0 to 20)

    # Academic Performance - 2nd Semester
    curricular_units_2nd_sem_approved: int                # Number of subjects passed in the 2nd semester
    curricular_units_2nd_sem_grade: float                 # Average grade in 2nd semester (Scale: 0 to 20)
    curricular_units_2nd_sem_without_evaluations: int     # Number of units where the student didn't take an exam (Scale: 0 to 20)


# define output (the structure of API response)
class PredictionOutput(BaseModel):
    prediction: str
    probability: float


# helper function (convert numeric model output into human-readable labels)
def map_prediction(pred):
    mapping = {
        0: "Dropout",
        1: "Graduate"
    }
    return mapping[pred]


# root endpoint (API Welcome Message)
# used to check if API is running
@app.get("/")
def root():
    return {
        "message": "Student Dropout Risk Prediction API is running"
    }


# health check endpoint (checks if the model is loaded correctly)
@app.get("/health")
def health_check():
    return {
        "status": "OK",
        "model_loaded": model is not None
    }


# prediction endpoint (MAIN ENDPOINT)
# receives student data and returns prediction
@app.post("/predict", response_model=PredictionOutput)
def predict_dropout(data: StudentInput):
    # Convert input data to DataFrame
    input_df = pd.DataFrame([data.dict()])
    # Make prediction
    prediction = model.predict(input_df)[0]
    # Get the probability of the predicted class
    probability = model.predict_proba(input_df).max()
    # Prepare response
    return {
        "prediction": map_prediction(prediction),
        "probability": round(float(probability), 2)
    }


# run the app with Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)