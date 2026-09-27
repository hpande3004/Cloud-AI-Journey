import boto3
from botocore.exceptions import ClientError


PROFILE_NAME = "cloud-ai-dev"
REGION = "us-east-1"


session = boto3.Session(
    profile_name=PROFILE_NAME,
    region_name=REGION
)

ec2 = session.client("ec2")


def list_instances():

    print("\nEC2 Instances")
    print("-" * 60)

    try:
        response = ec2.describe_instances()

        found = False

        for reservation in response["Reservations"]:

            for instance in reservation["Instances"]:

                found = True

                print(f"Instance ID : {instance['InstanceId']}")
                print(f"State       : {instance['State']['Name']}")
                print(f"Type        : {instance['InstanceType']}")

                print(
                    f"Private IP  : "
                    f"{instance.get('PrivateIpAddress', 'N/A')}"
                )

                print(
                    f"Public IP   : "
                    f"{instance.get('PublicIpAddress', 'N/A')}"
                )

                print("-" * 60)

        if not found:
            print("No EC2 instances found.")

    except ClientError as error:
        print(f"Error: {error}")


def main():

    print("==============================")
    print("       EC2 MANAGER")
    print("==============================")

    list_instances()


if __name__ == "__main__":
    main()