import requests

url = "http://localhost:5055/webhook/"

payload="{ \"next_action\": \"action_session_start\", \"tracker\": { \"sender_id\":\"default\" } }"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)