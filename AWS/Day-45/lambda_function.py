import json
import boto3
from botocore.exceptions import ClientError


TABLE_NAME = "CloudAI-Students-Day45"

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }


def lambda_handler(event, context):

    print("Received event:")
    print(json.dumps(event))

    method = event["requestContext"]["http"]["method"]
    path = event.get("rawPath", "")

    try:

        # CREATE STUDENT
        if method == "POST" and path == "/students":

            body = json.loads(event.get("body", "{}"))

            student_id = body.get("StudentID")
            name = body.get("Name")
            course = body.get("Course")

            if not student_id or not name or not course:
                return response(
                    400,
                    {"message": "StudentID, Name and Course are required"}
                )

            table.put_item(
                Item={
                    "StudentID": student_id,
                    "Name": name,
                    "Course": course
                },
                ConditionExpression="attribute_not_exists(StudentID)"
            )

            return response(
                201,
                {"message": "Student created successfully"}
            )

        # GET ALL STUDENTS
        elif method == "GET" and path == "/students":

            result = table.scan()

            return response(
                200,
                result.get("Items", [])
            )

        # GET ONE STUDENT
        elif method == "GET" and path.startswith("/students/"):

            student_id = event.get(
                "pathParameters",
                {}
            ).get("id")

            result = table.get_item(
                Key={
                    "StudentID": student_id
                }
            )

            student = result.get("Item")

            if not student:
                return response(
                    404,
                    {"message": "Student not found"}
                )

            return response(
                200,
                student
            )

        # DELETE STUDENT
        elif method == "DELETE" and path.startswith("/students/"):

            student_id = event.get(
                "pathParameters",
                {}
            ).get("id")

            table.delete_item(
                Key={
                    "StudentID": student_id
                }
            )

            return response(
                200,
                {"message": "Student deleted successfully"}
            )

        else:

            return response(
                404,
                {"message": "Route not found"}
            )

    except ClientError as error:

        error_code = error.response["Error"]["Code"]

        if error_code == "ConditionalCheckFailedException":
            return response(
                409,
                {"message": "Student already exists"}
            )

        print(error)

        return response(
            500,
            {"message": "AWS service error"}
        )

    except Exception as error:

        print(error)

        return response(
            500,
            {"message": "Internal server error"}
        )