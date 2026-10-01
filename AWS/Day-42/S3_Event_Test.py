import boto3
from botocore.exceptions import ClientError


PROFILE_NAME = "cloud-ai-dev"
REGION = "us-east-1"

BUCKET_NAME = "harshit-cloud-ai-day42-2026"
FILE_NAME = "test_upload.txt"


session = boto3.Session(
    profile_name=PROFILE_NAME,
    region_name=REGION
)

s3 = session.client("s3")


def upload_file():

    print("\nUploading file to S3...")

    try:

        s3.upload_file(
            FILE_NAME,
            BUCKET_NAME,
            FILE_NAME
        )

        print("Upload successful.")
        print(f"Bucket: {BUCKET_NAME}")
        print(f"File: {FILE_NAME}")

    except ClientError as error:

        print(f"Upload failed: {error}")


def main():

    print("==============================")
    print("       S3 EVENT TEST")
    print("==============================")

    upload_file()


if __name__ == "__main__":
    main()