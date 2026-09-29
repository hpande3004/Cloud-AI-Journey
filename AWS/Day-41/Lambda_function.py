import json


def lambda_handler(event, context):

    name = event.get("name", "Cloud Engineer")

    message = f"Hello {name}! Your AWS Lambda function is working."

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message
        })
    }