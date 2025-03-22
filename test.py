import requests

# API Endpoint
url = "http://127.0.0.1:8000/adhd/test"

# Correct JSON format: {"responses": [...]}
data = {"responses": [2, 4, 5, 1, 3, 2, 5, 3, 4, 2]}

# Send POST request with JSON body
response = requests.post(url, json=data)  # ✅ Correct JSON format

# Print Response
print(response.status_code)  # Should print 200 if successful
print(response.json())  # Should return test results
