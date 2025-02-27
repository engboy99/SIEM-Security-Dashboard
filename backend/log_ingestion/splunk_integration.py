import requests
import os

def send_to_splunk(log_data):
    url = "http://localhost:8088/services/collector/event"
    headers = {"Authorization": f"Splunk {os.getenv('SPLUNK_HEC_TOKEN')}"}
    payload = {
        "event": log_data,
        "sourcetype": "json",
        "index": "main"
    }
    response = requests.post(url, headers=headers, json=payload)
    print(f"Sent to Splunk: {response.status_code}")
