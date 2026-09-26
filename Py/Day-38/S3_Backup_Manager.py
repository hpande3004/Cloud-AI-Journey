import os
import boto3
import logging
from botocore.exceptions import ClientError


# -----------------------------
# Configuration
# -----------------------------

PROFILE_NAME = "cloud-ai-dev"
REGION = "ap-south-1"

BUCKET_NAME = "harshit-cloud-ai-day38-2026"

SOURCE_FOLDER = "backup_source"


# -----------------------------
# Logging
# -----------------------------

logging.basicConfig(
    filename="s3_backup.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# -----------------------------
# AWS Connection
# -----------------------------

session = boto3.Session(
    profile_name=PROFILE_NAME,
    region_name=REGION
)

s3 = session.client("s3")


# -----------------------------
# List Local Files
# -----------------------------

def get_local_files():

    files = []

    for filename in os.listdir(SOURCE_FOLDER):

        filepath = os.path.join(
            SOURCE_FOLDER,
            filename
        )

        if os.path.isfile(filepath):
            files.append(filepath)

    return files


# -----------------------------
# Upload Files
# -----------------------------

def upload_files():

    files = get_local_files()

    if not files:

        print("No files found.")

        return

    for filepath in files:

        filename = os.path.basename(filepath)

        try:

            s3.upload_file(
                filepath,
                BUCKET_NAME,
                filename
            )

            print(
                f"Uploaded: {filename}"
            )

            logging.info(
                f"Uploaded {filename}"
            )

        except FileNotFoundError:

            print(
                f"File not found: {filepath}"
            )

        except ClientError as error:

            print(
                f"Upload failed: {filename}"
            )

            logging.error(
                f"Upload failed: {filename} - {error}"
            )


# -----------------------------
# List S3 Objects
# -----------------------------

def list_s3_objects():

    print("\nFiles currently in S3:")

    try:

        response = s3.list_objects_v2(
            Bucket=BUCKET_NAME
        )

        objects = response.get(
            "Contents",
            []
        )

        if not objects:

            print("Bucket is empty.")

            return

        for obj in objects:

            print(
                f"- {obj['Key']} "
                f"({obj['Size']} bytes)"
            )

    except ClientError as error:

        print(
            f"Unable to list S3 objects: {error}"
        )

        logging.error(
            f"S3 listing failed: {error}"
        )


# -----------------------------
# Main
# -----------------------------

def main():

    print("==============================")
    print("      S3 BACKUP MANAGER")
    print("==============================")

    print("\nUploading files...")

    upload_files()

    list_s3_objects()

    print("\nBackup operation completed.")


if __name__ == "__main__":

    main()