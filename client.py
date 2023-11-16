# A simple HTTP client
import requests
import time

# Assuming the server service is named 'server' in docker-compose.yml
server_url = "http://server:8000"
# server_url = "http://127.0.0.1:8000"


while True:
    try:
        response = requests.get(server_url, timeout=10)
        print(f"Received response from server: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to server: {e}")
    time.sleep(5)  # Wait for 5 seconds before trying again
