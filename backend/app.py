from flask import Flask, jsonify, request
from models.threat_detection import detect_anomaly

app = Flask(__name__)

logs = []

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(logs)

@app.route('/logs', methods=['POST'])
def add_log():
    data = request.json
    anomaly = detect_anomaly(data["features"])
    data["anomaly"] = bool(anomaly)
    logs.append(data)
    return jsonify({"message": "Log added", "anomaly": anomaly})

if __name__ == '__main__':
    app.run(debug=True)
