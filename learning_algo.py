import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.externals import joblib
class SmartGridLearningAlgorithm:
    def __init__(self):
        self.scaler = MinMaxScaler()
        self.model = LinearRegression()
    def preprocess_data(self, data):
        normalized_data = self.scaler.fit_transform(data)
        return normalized_data
    def train_model(self, X, y):
        self.model.fit(X, y)
    def predict_demand(self, current_data):
        # Preprocess the current data
        normalized_data = self.scaler.transform([current_data])
        # Make predictions using the trained model
        predicted_demand = self.model.predict(normalized_data)
        predicted_demand = np.maximum(predicted_demand, 0)
        return predicted_demand
    def save_model(self, filename="smart_grid_model.pkl"):
        joblib.dump(self.model, filename)
    def load_model(self, filename="smart_grid_model.pkl"):
        self.model = joblib.load(filename)
X_train = np.array([[...], [...], ...])  # Features
y_train = np.array([...])  # Target variable (e.g., demand)
smart_grid_model = SmartGridLearningAlgorithm()
X_train_normalized = smart_grid_model.preprocess_data(X_train)
smart_grid_model.train_model(X_train_normalized, y_train)
smart_grid_model.save_model()
current_data = np.array([...])
predicted_demand = smart_grid_model.predict_demand(current_data)
print("Predicted Demand:", predicted_demand)
