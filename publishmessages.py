import functions_framework
import requests
import json
import time

from google.cloud import pubsub_v1
API_KEY = ""
STOCKS = ['AAPL','MSFT','NVDA','AMZN','GOOGL']
API_URL = "https://www.alphavantage.co/query"
PROJECT_ID = ""
TOPIC_ID = ""

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

def publish_to_pubsub(data):
    payload = json.dumps(data).encode("utf-8")
    future = publisher.publish(topic_path, payload)
    print(f"Published message ID: {future.result()}")


@functions_framework.http
def hello_http(request):
    auth.authenticate_user(project_id=PROJECT_ID)
for stock in STOCKS:
  time.sleep(3)
  params = {
    "function": "GLOBAL_QUOTE",
    "symbol": stock,
    "apikey": API_KEY
  }


  response = requests.get(API_URL, params=params)
  if response.status_code == 200:
    data = response.json()
    print(f"--- Live Global Quote for {stock} ---")
    print(json.dumps(data, indent=4))
    publish_to_pubsub({
            "symbol": stock,
            "data": data
        })
  else:
    print(f"Request failed with status code: {response.status_code}")
