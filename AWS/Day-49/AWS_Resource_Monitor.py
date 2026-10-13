import boto3
import json

# AWS Region
REGION = "us-east-1"

# Initialize AWS clients
ec2 = boto3.client("ec2", region_name=REGION)
s3 = boto3.client("s3")


def monitor_ec2():
    print("\n===== EC2 INSTANCE MONITOR =====")

    instances = []

    paginator = ec2.get_paginator("describe_instances")

    for page in paginator.paginate():
        for reservation in page["Reservations"]:
            for instance in reservation["Instances"]:
                instance_id = instance["InstanceId"]
                state = instance["State"]["Name"]

                print(f"Instance ID: {instance_id}")
                print(f"State: {state}")

                instances.append({
                    "InstanceId": instance_id,
                    "State": state
                })

    if not instances:
        print("No EC2 instances found.")

    return instances


def monitor_s3():
    print("\n===== S3 BUCKET MONITOR =====")

    response = s3.list_buckets()
    buckets = []

    for bucket in response.get("Buckets", []):
        bucket_name = bucket["Name"]

        print(f"Bucket: {bucket_name}")
        buckets.append(bucket_name)

    if not buckets:
        print("No S3 buckets found.")

    return buckets


def lambda_handler(event, context):
    print("Starting AWS Resource Monitoring...")

    ec2_instances = monitor_ec2()
    s3_buckets = monitor_s3()

    result = {
        "EC2Instances": ec2_instances,
        "S3Buckets": s3_buckets
    }

    print("\nMonitoring completed successfully!")
    print(json.dumps(result, indent=4))

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }


# Allow the script to run locally
if __name__ == "__main__":
    lambda_handler({}, None)
