import boto3
from botocore.exceptions import ClientError

PROFILE_NAME = "cloud-ai-dev"
REGION = "us-east-1"
TABLE_NAME = "CloudAI-Students-Day44"

# Connect to AWS DynamoDB
session = boto3.Session(
    profile_name=PROFILE_NAME,
    region_name=REGION
)

dynamodb = session.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)


# CREATE
def add_student():
    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Student Name: ").strip()
    course = input("Enter Course: ").strip()

    if not student_id or not name or not course:
        print("All fields are required.")
        return

    try:
        table.put_item(
            Item={
                "StudentID": student_id,
                "Name": name,
                "Course": course
            },
            ConditionExpression="attribute_not_exists(StudentID)"
        )
        print("Student added successfully!")

    except ClientError as error:
        if error.response["Error"]["Code"] == "ConditionalCheckFailedException":
            print("Student ID already exists!")
        else:
            print(f"Error: {error}")


# READ
def view_student():
    student_id = input("Enter Student ID: ").strip()

    try:
        response = table.get_item(
            Key={"StudentID": student_id}
        )

        student = response.get("Item")

        if student:
            print("\nStudent Details:")
            print(f"ID: {student['StudentID']}")
            print(f"Name: {student['Name']}")
            print(f"Course: {student['Course']}")
        else:
            print("Student not found.")

    except ClientError as error:
        print(f"Error: {error}")


# UPDATE
def update_student():
    student_id = input("Enter Student ID: ").strip()
    new_course = input("Enter New Course: ").strip()

    if not student_id or not new_course:
        print("Both fields are required.")
        return

    try:
        table.update_item(
            Key={"StudentID": student_id},
            UpdateExpression="SET Course = :course",
            ConditionExpression="attribute_exists(StudentID)",
            ExpressionAttributeValues={
                ":course": new_course
            }
        )

        print("Student updated successfully!")

    except ClientError as error:
        if error.response["Error"]["Code"] == "ConditionalCheckFailedException":
            print("Student not found.")
        else:
            print(f"Error: {error}")


# DELETE
def delete_student():
    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        print("Student ID is required.")
        return

    try:
        table.delete_item(
            Key={"StudentID": student_id},
            ConditionExpression="attribute_exists(StudentID)"
        )

        print("Student deleted successfully!")

    except ClientError as error:
        if error.response["Error"]["Code"] == "ConditionalCheckFailedException":
            print("Student not found.")
        else:
            print(f"Error: {error}")


# VIEW ALL
def view_all_students():
    print("\n=== All Students ===")

    try:
        students = []
        response = table.scan()
        students.extend(response.get("Items", []))

        while "LastEvaluatedKey" in response:
            response = table.scan(
                ExclusiveStartKey=response["LastEvaluatedKey"]
            )
            students.extend(response.get("Items", []))

        if not students:
            print("No student records found.")
            return

        for student in students:
            print(
                f"ID: {student['StudentID']} | "
                f"Name: {student['Name']} | "
                f"Course: {student['Course']}"
            )

    except ClientError as error:
        print(f"Error: {error}")


# MAIN MENU
def main():
    while True:
        print("\n================================")
        print("    DYNAMODB STUDENT MANAGER")
        print("================================")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. View All Students")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_student()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            view_all_students()

        elif choice == "6":
            print("Exiting Student Manager.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()