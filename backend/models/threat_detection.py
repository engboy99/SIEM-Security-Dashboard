from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Example data for training (log features, labels)
log_data = np.array([[1.1, 0.1], [1.2, 0.2], [1.3, 0.3], [3.0, 2.0]])  # Features
labels = [0, 0, 0, 1]  # 0 = Normal, 1 = Anomaly

# Train the Random Forest model
model = RandomForestClassifier(n_estimators=100)
model.fit(log_data, labels)

def detect_anomaly(features):
    return model.predict([features])[0]
