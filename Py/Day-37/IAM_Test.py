# import boto3

# session = boto3.Session(
#     profile_name="cloud-ai-dev",
#     region_name="ap-south-1"
# )

# sts = session.client("sts")

# identity = sts.get_caller_identity()

# print("AWS IAM authentication successful!")
# print(f"Account: {identity['Account']}")
# print(f"User ID: {identity['UserId']}")
# print(f"ARN: {identity['Arn']}")
#----------------------------------------------

import boto3

session = boto3.Session(
    profile_name="cloud-ai-dev",
    region_name="ap-south-1"
)

s3 = session.client("s3")

print("S3 access successful!")

response = s3.list_buckets()

for bucket in response.get("Buckets", []):
    print(bucket["Name"])