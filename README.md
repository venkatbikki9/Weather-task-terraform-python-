# Weather Data Collection System :

This project collects real-time weather information for multiple cities and stores the results in an AWS S3 bucket. The goal is to demonstrate how API integration, Python development, AWS services, and Infrastructure as Code can work together in a small DevOps-style workflow.

## Features :

1. Fetches live weather data from the OpenWeather API

2. Supports multiple cities

3. Converts weather response into JSON files

4. Uploads these Json files to Amazon S3

5. JSON files include timestamps for historical tracking

6. Terraform creates the S3 bucket and configures access

7. Environment variables used for credentials and configuration

## Project Structure :
weather-project/

│

├── src/

│     ├── weather.py

│     ├── utils.py

│     ├── requirements.txt

│     ├── .env.example

│

├── data/                (JSON files generated here)

│

├── infra/               (Terraform infrastructure code)

│     ├── main.tf

│     ├── variables.tf

│     ├── outputs.tf

│

└── README.md

## Technologies Used -

Python 3.x

OpenWeather API

AWS S3 for storing weather logs

Terraform for creating and configuring the S3 bucket

boto3 (AWS SDK for Python)

requests

python-dotenv

## Setup-
1. Create and activate the virtual environment

python3 -m venv venv

source venv/bin/activate

2. Install Python dependencies

pip install -r src/requirements.txt

3. Set up environment variables


Inside src/.env - change these variables

```
+------------------------------------------------------------------------+
OPENWEATHER_API_KEY=your_api_key
Go to the OpenWeather website and create an account.
Then log in and go to the API Keys page.
The API key is available there.
+------------------------------------------------------------------------+

AWS_ACCESS_KEY_ID=your_access_key
Go to the AWS Console and search for IAM.
Create a user.
It will generate the AWS Access Key ID and Secret Access Key.
+------------------------------------------------------------------------+

AWS_SECRET_ACCESS_KEY=your_secret_key
Generated along with the AWS Access Key ID.
+------------------------------------------------------------------------+

AWS_REGION=ap-south-1
Change the region in the AWS Console depending on your location.
+------------------------------------------------------------------------+

S3_BUCKET_NAME=your_bucket_name
Give a bucket name.
+------------------------------------------------------------------------+

CITIES=Delhi,Hyderabad,Mumbai
Add the names of the cities for which weather data is required.
+------------------------------------------------------------------------+

```
4. Deploy Infrastructure with Terraform

Go to the infra/ folder:

cd infra

terraform init

<img width="1920" height="1080" alt="1  initializing terraform" src="https://github.com/user-attachments/assets/1577089b-8050-40db-ac84-40eedf34181d" />

terraform apply

<img width="1920" height="1080" alt="2  terraform apply" src="https://github.com/user-attachments/assets/72a5d7a4-d095-4be8-a338-d472d4412c70" />

Terraform will create:

S3 bucket

ACL settings

Public access configuration

Bucket policy

After this step, your bucket is ready to receive uploaded JSON files.

5. Run the Weather Collector

cd src

python3 weather.py

<img width="1920" height="1080" alt="3  python app" src="https://github.com/user-attachments/assets/929aea2c-819e-4144-950d-b324b3427e9a" />

The script will:

Fetch weather for each city

Save JSON output inside the data/ folder

Upload each JSON file to your S3 bucket

Print the public URL of each uploaded file

## SCREENSHOTS 

<img width="1920" height="1024" alt="4  S3 bucket" src="https://github.com/user-attachments/assets/1c59b8b4-49bc-490a-b4a6-54fe2ccae8ae" />

<img width="1920" height="1016" alt="5  S3 bucket objects" src="https://github.com/user-attachments/assets/e4300f79-a0a8-41dc-a864-b22cb4f5bc80" />

<img width="1920" height="1022" alt="6  one of the objects" src="https://github.com/user-attachments/assets/7900106d-e314-4bf2-aa19-d04b9ba85e44" />

<img width="1920" height="1018" alt="7  above object URL" src="https://github.com/user-attachments/assets/ebbcf343-baab-4180-8fc3-325722d48676" />

