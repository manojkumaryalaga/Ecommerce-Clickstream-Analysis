import boto3
import json
import time
import random
from datetime import datetime, timezone

# Configure AWS region and bucket
REGION = 'us-east-2'
BUCKET = 'manoj-ecommerce-raw-data'

# Initialize S3 client
s3 = boto3.client('s3', region_name=REGION)

def generate_click_event():
    return {
        "user_id": random.randint(1, 1000),
        "session_id": f"session-{random.randint(1000, 9999)}",
        "event_type": random.choice(["click", "view", "add_to_cart", "purchase"]),
        "page": random.choice(["home", "product", "cart", "checkout"]),
        "product_id": random.randint(1, 500),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_time": int(datetime.now(timezone.utc).timestamp()),
        "device_type": random.choice(["desktop", "mobile", "tablet"]),
        "referrer_url": random.choice(["https://google.com", "https://facebook.com", "https://twitter.com", "https://email.campaign.com"]),
        "location": random.choice(["New York, USA", "London, UK", "Berlin, Germany", "Mumbai, India", "Tokyo, Japan"]),
        "browser": random.choice(["Chrome", "Firefox", "Safari", "Edge"]),
        "user_type": random.choice(["new", "returning"])
    }


def upload_event(event):
    # Use timestamp-based unique filename
    filename = f"logs/event-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%f')}.json"
    body = json.dumps(event).encode('utf-8')
    
    s3.put_object(Bucket=BUCKET, Key=filename, Body=body)
    print(f"Uploaded event to {filename}")

if __name__ == "__main__":
    try:
        while True:
            event = generate_click_event()
            upload_event(event)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped by user")
