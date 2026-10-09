import boto3

# Connect to Amazon SQS
sqs = boto3.client("sqs", region_name="us-east-1")

# Get our existing queue
response = sqs.get_queue_url(
    QueueName="cloud-ai-day46-queue"
)

queue_url = response["QueueUrl"]

# Send a message
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody="Hello from Python! This is Day 46 of Cloud-AI-Journey."
)

print("Message sent successfully!")
print("Message ID:", response["MessageId"])

#-----------------------------------------------------------------------------

# Receive messages from SQS
response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1,
    WaitTimeSeconds=10
)

messages = response.get("Messages", [])

if messages:
    if messages:
        for message in messages:
            print("\nMessage received!")
            print("Message ID:", message["MessageId"])
            print("Message Body:", message["Body"])

        # Simulate processing the message
            print("Processing message...")

        # Delete the message after successful processing
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=message["ReceiptHandle"]
        )

            print("Message processed and deleted successfully!")

else:
    print("No messages available.")