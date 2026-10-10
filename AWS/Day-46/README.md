
# Day 46 - Amazon SQS Automation with Python

## Project Overview

Built a Python-based message queue management application using Amazon Simple Queue Service (SQS) and Boto3.

The project demonstrates how to send, receive, and delete messages from an AWS SQS queue using Python.

## AWS Services Used

- Amazon SQS - Message queuing service
- AWS IAM - Access and permission management

## Technologies

- Python 3
- Boto3
- AWS CLI
- AWS Management Console

## Architecture

Python Producer
      |
      v
 Amazon SQS Queue
      |
      v
Python Consumer
      |
      v
Message Processing
      |
      v
Message Deletion

## Features

- Connect to Amazon SQS using Boto3
- Retrieve an existing SQS queue URL
- Send messages to an SQS queue
- Receive messages from the queue
- Delete messages after processing
- Implement basic asynchronous messaging

## How to Run

### 1. Configure AWS Credentials

Configure your AWS CLI with appropriate IAM permissions.

### 2. Create an SQS Queue

Create a Standard SQS queue named:

`cloud-ai-day46-queue`

Region: `us-east-1`

### 3. Install Dependencies

```bash
pip install boto3
```

### 4. Execute the Python Script

```bash
python SQS_Manager.py
```

## Expected Output

The Python application should:

1. Connect to Amazon SQS.
2. Retrieve the queue URL.
3. Send a message to the queue.
4. Receive the message.
5. Delete the message after processing.

## Key Learnings

- SQS is a fully managed message queuing service.
- Producers send messages to a queue.
- Consumers retrieve and process messages.
- Messages are temporarily hidden during the visibility timeout.
- Successfully processed messages should be deleted using their receipt handles.
- SQS enables asynchronous communication between application components.
- Boto3 allows Python applications to interact with AWS services programmatically.

## Important Concepts

### Standard Queue
Provides high throughput with at-least-once delivery and best-effort ordering.

### Visibility Timeout
Temporarily hides a received message from other consumers while it is being processed.

### Message Retention
Defines how long messages remain in the queue before automatic deletion.

### Long Polling
Allows consumers to wait for messages instead of repeatedly making empty requests.

## Cleanup

Deleted the temporary SQS queue after completing the project to avoid unnecessary resource usage.

## Conclusion

Successfully implemented basic Amazon SQS message operations using Python and Boto3, gaining practical experience with asynchronous messaging and cloud automation.
