import requests
import boto3
import os
from dotenv import load_dotenv
from utils import save_json

# Load .env variables
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BUCKET = os.getenv("S3_BUCKET_NAME")
REGION = os.getenv("AWS_REGION")
CITIES = os.getenv("CITIES").split(",")

# AWS Client
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=REGION
)

def fetch_weather(city):
    """Fetch weather from OpenWeather API."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    except Exception as e:
        print(f"❌ Error fetching weather for {city}: {e}")
        return None

def upload_to_s3(filepath):
    """Upload JSON file to S3 with correct Content-Type and ACL."""
    try:
        filename = filepath.split("/")[-1]

        s3.upload_file(
            filepath,
            BUCKET,
            filename,
            ExtraArgs={
                "ContentType": "application/json",
                "ACL": "public-read"
            }
        )

        print(f"✅ Uploaded to S3 (public): {filename}")

        object_url = f"https://{BUCKET}.s3.{REGION}.amazonaws.com/{filename}"
        print(f"🌐 URL: {object_url}")

    except Exception as e:
        print(f"❌ Upload Error: {e}")

def main():
    for city in CITIES:
        print(f"\n🌤 Fetching weather for {city}...")
        data = fetch_weather(city)

        if data:
            filepath = save_json(data, city)
            upload_to_s3(filepath)

if __name__ == "__main__":
    main()
