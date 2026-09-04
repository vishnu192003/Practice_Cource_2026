import numpy as np
from sklearn.linear_model import LinearRegression
from fastapi import FastAPI
from pydantic import BaseModel


# ----------------- 1. AI ENGINE CLASS -----------------
class SalaryPredictor:
    def __init__(self):
        self.model = LinearRegression()

    def train(self):
        X = np.array([1, 2, 3, 4]).reshape(-1, 1)
        y = np.array([10, 20, 30, 40])
        self.model.fit(X, y)
        print("Model trained successfully inside the class!")

    def predict_salary(self, experience: float):
        input_data = np.array([[experience]])
        prediction = self.model.predict(input_data)
        return float(prediction[0])  # [0] लगाने से NumPy की Warning हट जाएगी


# ----------------- 2. FASTAPI SETUP -----------------
app = FastAPI(title="AI/ML Salary Prediction API")

# सर्वर चालू होते ही मॉडल बैकग्राउंड में ट्रेन हो जाएगा
predictor = SalaryPredictor()
predictor.train()


# इनपुट डेटा का फॉर्मेट तय करना
class InputData(BaseModel):
    experience: float


# इंटरनेट पर लाइव यूआरएल (Endpoint) बनाना
@app.post("/predict")
def get_prediction(data: InputData):
    predicted_val = predictor.predict_salary(data.experience)
    return {
        "status": "success",
        "input_experience": data.experience,
        "predicted_salary_in_k": predicted_val,
    }
