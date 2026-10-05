import boto3
from botocore.exceptions import ClientError


PROFILE_NAME = "cloud-ai-dev"
REGION = "us-east-1"


session = boto3.Session(
    profile_name=PROFILE_NAME,
    region_name=REGION
)

logs = session.client("logs")
cloudwatch = session.client("cloudwatch")


def list_log_groups():

    print("\n=== CLOUDWATCH LOG GROUPS ===")

    try:
        response = logs.describe_log_groups()

        groups = response.get("logGroups", [])

        if not groups:
            print("No log groups found.")
            return

        for group in groups:
            print(
                f"Log Group: "
                f"{group['logGroupName']}"
            )

    except ClientError as error:
        print(f"Error: {error}")


def list_ec2_metrics():

    print("\n=== EC2 CLOUDWATCH METRICS ===")

    try:
        response = cloudwatch.list_metrics(
            Namespace="AWS/EC2"
        )

        metrics = response.get("Metrics", [])

        if not metrics:
            print("No EC2 metrics found.")
            return

        for metric in metrics[:10]:
            print(
                f"Metric: {metric['MetricName']}"
            )

    except ClientError as error:
        print(f"Error: {error}")


def main():

    print("==============================")
    print("     CLOUDWATCH MANAGER")
    print("==============================")

    list_log_groups()
    list_ec2_metrics()


if __name__ == "__main__":
    main()