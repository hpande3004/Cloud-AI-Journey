
import json
import os
from urllib.parse import unquote_plus

import boto3

# Connect to Amazon SNS
sns = boto3.client("sns")

# Read SNS topic ARN from Lambda environment variables
SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN")


def lambda_handler(event, context):

    if not SNS_TOPIC_ARN:
        raise ValueError("SNS_TOPIC_ARN environment variable is missing")

    # Read each S3 event record
    for record in event["Records"]:

        # Extract S3 bucket and uploaded file information
        bucket_name = record["s3"]["bucket"]["name"]
        file_name = unquote_plus(record["s3"]["object"]["key"])

        print(f"New file uploaded: {file_name}")
        print(f"S3 Bucket: {bucket_name}")

        # Prepare notification
        subject = "Day 48 - New S3 File Uploaded"

        message = (
            f"A new file has been uploaded to Amazon S3.\n\n"
            f"Bucket: {bucket_name}\n"
            f"File: {file_name}\n\n"
            f"Notification generated automatically using AWS Lambda."
        )

        # Publish notification to SNS
        response = sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=subject,
            Message=message
        )

        print("SNS Notification Published!")
        print("Message ID:", response["MessageId"])

    return {
        "statusCode": 200,
        "body": json.dumps("S3 event processed successfully")
    }
