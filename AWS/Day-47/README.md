
# Day 47 - Amazon SNS with Python and SQS Integration

## Project Overview
Implemented a notification system using Amazon SNS, Amazon SQS, and Python Boto3.

The project demonstrates how a single notification can be distributed to multiple subscribers using SNS fan-out messaging.

## AWS Services Used
- Amazon SNS - Publish and distribute notifications
- Amazon SQS - Receive and store messages
- AWS IAM - Manage access permissions

## Technologies
- Python 3
- Boto3
- AWS CLI
- AWS Management Console

## Architecture

Python Publisher
       |
       v
   Amazon SNS
       |
       +----> Email Subscriber
       |
       +----> Amazon SQS Queue

## Features
- Connect to Amazon SNS using Boto3
- Discover an existing SNS topic
- Publish notifications using Python
- Accept dynamic subject and message input
- Deliver notifications to email and SQS subscribers

## How to Run

1. Configure AWS credentials using the AWS CLI.
2. Create an SNS topic named `cloud-ai-day47-topic`.
3. Subscribe and confirm an email address.
4. Create an SQS queue and subscribe it to the SNS topic.
5. Configure the SQS access policy to allow SNS delivery.
6. Install Boto3:

   pip install boto3

7. Execute the script:

   python SNS_Manager.py

8. Enter the notification subject and message.

## Expected Output
- A notification is published successfully.
- The email subscriber receives the notification.
- The SQS queue receives a copy of the message.

## Key Learnings
- SNS follows a publish-subscribe messaging model.
- SQS provides message queuing for asynchronous processing.
- SNS fan-out enables delivery to multiple subscribers.
- Boto3 allows AWS messaging services to be controlled using Python.

## Cleanup
Deleted the temporary SNS topic, subscriptions, and SQS queue after testing.
