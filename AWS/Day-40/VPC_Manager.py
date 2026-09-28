import boto3
from botocore.exceptions import ClientError


PROFILE_NAME = "cloud-ai-dev"
REGION = "us-east-1"


session = boto3.Session(
    profile_name=PROFILE_NAME,
    region_name=REGION
)

ec2 = session.client("ec2")


def list_vpcs():
    print("\n=== VPCs ===")

    try:
        response = ec2.describe_vpcs()

        for vpc in response["Vpcs"]:
            print(
                f"VPC ID: {vpc['VpcId']} | "
                f"CIDR: {vpc['CidrBlock']} | "
                f"Default: {vpc.get('IsDefault', False)}"
            )

    except ClientError as error:
        print(f"VPC error: {error}")


def list_subnets():
    print("\n=== Subnets ===")

    try:
        response = ec2.describe_subnets()

        for subnet in response["Subnets"]:
            print(
                f"Subnet ID: {subnet['SubnetId']} | "
                f"CIDR: {subnet['CidrBlock']} | "
                f"AZ: {subnet['AvailabilityZone']} | "
                f"VPC: {subnet['VpcId']}"
            )

    except ClientError as error:
        print(f"Subnet error: {error}")


def list_route_tables():
    print("\n=== Route Tables ===")

    try:
        response = ec2.describe_route_tables()

        for table in response["RouteTables"]:
            print(
                f"Route Table: {table['RouteTableId']} | "
                f"VPC: {table['VpcId']}"
            )

            for route in table["Routes"]:
                destination = route.get(
                    "DestinationCidrBlock",
                    "N/A"
                )

                gateway = route.get(
                    "GatewayId",
                    "local"
                )

                print(
                    f"  {destination} -> {gateway}"
                )

    except ClientError as error:
        print(f"Route table error: {error}")


def list_internet_gateways():
    print("\n=== Internet Gateways ===")

    try:
        response = ec2.describe_internet_gateways()

        for gateway in response["InternetGateways"]:
            print(
                f"Internet Gateway: "
                f"{gateway['InternetGatewayId']}"
            )

            for attachment in gateway["Attachments"]:
                print(
                    f"  VPC: {attachment.get('VpcId')}"
                )

    except ClientError as error:
        print(f"Internet Gateway error: {error}")


def main():
    print("==============================")
    print("       VPC MANAGER")
    print("==============================")

    list_vpcs()
    list_subnets()
    list_route_tables()
    list_internet_gateways()


if __name__ == "__main__":
    main()