import boto3

# Step 1: Connect to Amazon SNS
sns = boto3.client("sns", region_name="us-east-1")

# Step 2: Find our existing SNS topic
response = sns.list_topics()

topic_arn = next(
    topic["TopicArn"]
    for topic in response["Topics"]
    if topic["TopicArn"].endswith(":cloud-ai-day47-topic")
)

# Step 3: Create a function to send notifications
def send_notification(subject, message):
    response = sns.publish(
        TopicArn=topic_arn,
        Subject=subject,
        Message=message
    )

    print("\nNotification sent successfully!")
    print("Message ID:", response["MessageId"])


# Step 4: Take input from the user
subject = input("Enter notification subject: ")
message = input("Enter notification message: ")

# Step 5: Publish the notification
send_notification(subject, message)