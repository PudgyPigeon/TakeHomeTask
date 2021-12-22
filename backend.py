import pandas as pd
import boto3
from dotenv import load_dotenv
import io
import os


# Load data into a custom variable to make it easier to access data throughout program
def load_data():

    # Load environemnt variables for AWS S3 keys
    load_dotenv()

    # ENV variables for AWS config
    aws_key = os.environ.get("AWS_KEY")
    aws_secret = os.environ.get("AWS_SECRET_KEY")

    # Assign specific bucket holding data to variable: s3
    s3 = boto3.resource(
        "s3", aws_access_key_id=aws_key, aws_secret_access_key=aws_secret
    )

    # Set up buffer
    buffer = io.BytesIO()

    # Get parquet file and read it into data variable
    object = s3.Object(bucket_name="myparq", key="minwage.parquet")
    object.download_fileobj(buffer)
    dataframe = pd.read_parquet(buffer)

    # Return data that Pandas has read
    return dataframe
