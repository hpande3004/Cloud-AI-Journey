import boto3
import json
from botocore.exceptions import ClientError


PROFILE_NAME = "cloud-ai-dev"
REGION = "us-east-1"
FUNCTION_NAME = "cloud-ai-day41-function"


session = boto3.Session(
    profile_name=PROFILE_NAME,
    region_name=REGION
)

lambda_client = session.client("lambda")


def list_functions():

    print("\n=== Lambda Functions ===")

    try:
        response = lambda_client.list_functions()

        for function in response["Functions"]:

            print(
                f"Name: {function['FunctionName']} | "
                f"Runtime: {function['Runtime']} | "
                f"Memory: {function['MemorySize']} MB"
            )

    except ClientError as error:
        print(f"Error listing functions: {error}")


def invoke_function():

    print("\n=== Invoking Lambda ===")

    payload = {
        "name": "Harshit"
    }

    try:
        response = lambda_client.invoke(
            FunctionName=FUNCTION_NAME,
            InvocationType="RequestResponse",
            Payload=json.dumps(payload)
        )

        result = json.loads(
            response["Payload"].read().decode("utf-8")
        )

        print("Status Code:", response["StatusCode"])
        print("Lambda Response:", result)

    except ClientError as error:
        print(f"Error invoking Lambda: {error}")


def main():

    print("==============================")
    print("       LAMBDA MANAGER")
    print("==============================")

    list_functions()
    invoke_function()


if __name__ == "__main__":
    main()