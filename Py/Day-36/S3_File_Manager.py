# import boto3

# sts = boto3.client("sts")

# identity = sts.get_caller_identity()

# print("AWS authentication successful!")
# print(f"Account: {identity['Account']}")
# print(f"User ID: {identity['UserId']}")
# print(f"ARN: {identity['Arn']}")
#---------------------------------------------------------
# import boto3

# s3 = boto3.client(
#     "s3",
#     region_name="ap-south-1"
# )

# response = s3.list_buckets()

# print("S3 connection successful!")

# for bucket in response["Buckets"]:
#     print(bucket["Name"])
#-------------------------------------------------------------------
# import boto3
# from botocore.exceptions import ClientError

# s3 = boto3.client(
#     "s3",
#     region_name="ap-south-1"
# )

# BUCKET_NAME = "harshit-cloud-ai-day36-2026"


# try:
#     s3.create_bucket(
#         Bucket=BUCKET_NAME,
#         CreateBucketConfiguration={
#             "LocationConstraint": "ap-south-1"
#         }
#     )

#     print(f"Bucket created successfully: {BUCKET_NAME}")

# except ClientError as error:
#     print(f"Failed to create bucket: {error}")
#---------------------------------------------------------------------
import boto3
import logging
from botocore.exceptions import ClientError


REGION = "ap-south-1"

BUCKET_NAME = "harshit-cloud-ai-day36-2026"

LOCAL_FILE = "test_upload.txt"

S3_OBJECT_NAME = "test_upload.txt"

DOWNLOADED_FILE = "downloaded_test_upload.txt"


logging.basicConfig(
    filename="s3_file_manager.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


s3 = boto3.client(
    "s3",
    region_name=REGION
)


def list_buckets():

    print("\n--- S3 BUCKETS ---")

    try:

        response = s3.list_buckets()

        buckets = response.get("Buckets", [])

        if not buckets:

            print("No buckets found.")
            return

        for bucket in buckets:

            print(bucket["Name"])

    except ClientError as error:

        logging.error(
            f"Failed to list buckets: {error}"
        )

        print(
            f"Failed to list buckets: {error}"
        )


def upload_file():

    print("\n--- UPLOAD FILE ---")

    try:

        s3.upload_file(
            LOCAL_FILE,
            BUCKET_NAME,
            S3_OBJECT_NAME
        )

        logging.info(
            f"Uploaded {LOCAL_FILE} "
            f"to {BUCKET_NAME}"
        )

        print(
            f"Uploaded {LOCAL_FILE} successfully."
        )

    except FileNotFoundError:

        print(
            f"File not found: {LOCAL_FILE}"
        )

    except ClientError as error:

        logging.error(
            f"Upload failed: {error}"
        )

        print(
            f"Upload failed: {error}"
        )


def list_objects():

    print("\n--- S3 OBJECTS ---")

    try:

        response = s3.list_objects_v2(
            Bucket=BUCKET_NAME
        )

        objects = response.get(
            "Contents",
            []
        )

        if not objects:

            print("No objects found.")
            return

        for obj in objects:

            print(
                f"Name: {obj['Key']} | "
                f"Size: {obj['Size']} bytes"
            )

    except ClientError as error:

        logging.error(
            f"Failed to list objects: {error}"
        )

        print(
            f"Failed to list objects: {error}"
        )


def download_file():

    print("\n--- DOWNLOAD FILE ---")

    try:

        s3.download_file(
            BUCKET_NAME,
            S3_OBJECT_NAME,
            DOWNLOADED_FILE
        )

        logging.info(
            f"Downloaded {S3_OBJECT_NAME}"
        )

        print(
            f"Downloaded file as "
            f"{DOWNLOADED_FILE}"
        )

    except ClientError as error:

        logging.error(
            f"Download failed: {error}"
        )

        print(
            f"Download failed: {error}"
        )


def delete_object():

    print("\n--- DELETE OBJECT ---")

    try:

        s3.delete_object(
            Bucket=BUCKET_NAME,
            Key=S3_OBJECT_NAME
        )

        logging.info(
            f"Deleted {S3_OBJECT_NAME}"
        )

        print(
            f"Deleted {S3_OBJECT_NAME} "
            f"from S3."
        )

    except ClientError as error:

        logging.error(
            f"Delete failed: {error}"
        )

        print(
            f"Delete failed: {error}"
        )


def main():

    print("==============================")
    print("       AWS S3 FILE MANAGER")
    print("==============================")

    list_buckets()

    upload_file()

    list_objects()

    download_file()

    delete_object()

    print("\n==============================")
    print("       OPERATION COMPLETE")
    print("==============================")


if __name__ == "__main__":
    main()