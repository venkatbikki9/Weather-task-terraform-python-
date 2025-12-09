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

OPENWEATHER_API_KEY=your_api_key         - Go to OpenWeather website and create an account.then log in and go to API Keys page.There API key is avaliable.

AWS_ACCESS_KEY_ID=your_access_key        - Go to AWS console and search for IAM. Then create a user there and it will generate AWS key ID and Secret access key.

AWS_SECRET_ACCESS_KEY=your_secret_key

AWS_REGION=ap-south-1                    - Change the region in the console depending on the region.

S3_BUCKET_NAME=your_bucket_name          - Give a bucket name

CITIES=Delhi,Hyderabad,Mumbai            - Add the names of the cities we need the weather data from.


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

<img width="1920" height="1080" alt="4  S3 bucket" src="https://github.com/user-attachments/assets/9fd25262-fbc1-4da9-a05c-eeb5f78fc4de" />

<img width="1920" height="1080" alt="5  S3 bucket objects" src="https://github.com/user-attachments/assets/701ce995-2ddb-4f55-8670-7f05fa98d233" />

<img width="1920" height="1080" alt="6  one of the objects" src="https://github.com/user-attachments/assets/9e682066-1793-4cb3-a8f0-0cdfad54cbf0" />

<img width="1920" height="1080" alt="7  above object URL" src="https://github.com/user-attachments/assets/8a29b8da-45e6-4e99-8d55-50ba4419ebfd" />
