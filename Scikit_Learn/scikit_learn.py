import numpy as np
from sklearn.linear_model import LinearRegression


class SalaryPredictor:
    def __init__(self):
        # 1. खाली मॉडल को इनिशियलाइज किया
        self.model = LinearRegression()

    def train(self):
        # 2. डमी डेटा (X = अनुभव, y = सैलरी)
        X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
        y = np.array([10, 20, 30, 40, 50])

        # 3. मॉडल को ट्रेन करना
        self.model.fit(X, y)
        print("Model trained successfully inside the class!")

    def predict_salary(self, experience: float):
        # 4. इनपुट को सही शेप में बदलकर प्रेडिक्ट करना
        input_data = np.array([[experience]])
        prediction = self.model.predict(input_data)
        return float(prediction[0])  # [0] लगाने से NumPy सीधा सिंगल एलिमेंट निकाल लेता है


# टेस्ट करने के लिए इंजन को चलाकर देखते हैं
if __name__ == "__main__":
    predictor = SalaryPredictor()
    predictor.train()
    result = predictor.predict_salary(6)  # 6 साल का अनुभव टेस्ट किया
    print(f"Prediction for 6 years experience: Rs. {result}k")
