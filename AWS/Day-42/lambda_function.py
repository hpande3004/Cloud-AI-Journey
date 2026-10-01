import json
import urllib.parse


def lambda_handler(event, context):

    print("S3 event received!")

    for record in event["Records"]:

        bucket_name = record["s3"]["bucket"]["name"]

        object_key = urllib.parse.unquote_plus(
            record["s3"]["object"]["key"]
        )

        object_size = record["s3"]["object"].get(
            "size",
            "Unknown"
        )

        print(f"Bucket: {bucket_name}")
        print(f"File: {object_key}")
        print(f"Size: {object_size} bytes")

    return {
        "statusCode": 200,
        "body": json.dumps(
            "S3 event processed successfully"
        )
    }