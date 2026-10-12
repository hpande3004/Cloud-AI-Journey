
# Day 48 - AWS Event-Driven File Processing

## Project Overview

Built an event-driven file processing and notification system using Amazon S3, AWS Lambda, Amazon SNS, Amazon SQS, and Python.

Whenever a new file is uploaded to an S3 bucket, AWS Lambda is automatically triggered and publishes a notification to SNS, which distributes the message to email and SQS subscribers.

## AWS Services Used

- Amazon S3 - Object storage and event generation
- AWS Lambda - Serverless Python execution
- Amazon SNS - Publish-subscribe notification service
- Amazon SQS - Message queuing service
- AWS IAM - Access and permission management
- Amazon CloudWatch - Execution logging and monitoring

## Technologies

- Python 3.14 (AWS Lambda runtime)
- Boto3
- AWS Management Console

## Architecture

File Upload
     |
     v
 Amazon S3
     |
     | ObjectCreated Event
     v
 AWS Lambda
     |
     | sns.publish()
     v
 Amazon SNS
     |
     +------> Email Notification
     |
     +------> Amazon SQS Queue

## Project Structure

Day-48/
|
|-- S3_Event_Processor.py
|-- README.md
|-- test_upload.txt

## Features

- Automatically detects new S3 object uploads
- Triggers Lambda through S3 event notifications
- Extracts bucket name and object key
- Decodes URL-encoded S3 object keys
- Publishes notifications using Boto3
- Delivers notifications to email and SQS
- Records execution logs in CloudWatch
- Uses IAM permissions for secure service communication

## Implementation Steps

1. Created an S3 bucket for storing uploaded files.
2. Created an AWS Lambda function using Python 3.14.
3. Created an SNS Standard topic.
4. Configured and confirmed an email subscription.
5. Created an SQS Standard queue.
6. Subscribed the SQS queue to the SNS topic.
7. Configured the SQS access policy for SNS delivery.
8. Developed the Lambda function using Python and Boto3.
9. Configured the SNS_TOPIC_ARN environment variable.
10. Granted Lambda permission to publish to SNS.
11. Configured an S3 ObjectCreated event trigger.
12. Uploaded a sample file and verified the workflow.

## Lambda Configuration

Function name:
cloud-ai-day48-s3-processor

Runtime:
Python 3.14

Handler:
lambda_function.lambda_handler

Environment variable:
SNS_TOPIC_ARN = ARN of the SNS topic

Required IAM permissions:
- CloudWatch Logs permissions
- sns:Publish on the designated SNS topic

## Testing

Uploaded test_upload.txt to the S3 bucket.

Expected results:

1. S3 generates an ObjectCreated event.
2. Lambda executes automatically.
3. Lambda extracts the bucket and filename.
4. SNS publishes the notification.
5. Email subscriber receives the notification.
6. SQS queue receives the message.
7. CloudWatch records execution logs.

All components were successfully tested.

## Key Learnings

### Event-Driven Architecture
Applications respond automatically to events without requiring manual execution.

### Serverless Computing
AWS Lambda executes code without managing servers.

### S3 Event Notifications
Amazon S3 can invoke Lambda when objects are created.

### SNS Fan-out
One SNS notification can be delivered to multiple subscribers.

### Asynchronous Messaging
Amazon SQS stores messages for processing by consumers.

### IAM Execution Roles
Lambda requires its own permissions to access other AWS services.

### CloudWatch Logging
CloudWatch helps monitor and troubleshoot Lambda executions.

## Cleanup

Temporary AWS resources should be deleted after testing to avoid unnecessary charges.

Resources:
- S3 bucket and test object
- Lambda function
- SNS topic and subscriptions
- SQS queue
- Project-specific IAM execution role and policy

## Conclusion

Successfully implemented an event-driven serverless automation workflow integrating Amazon S3, AWS Lambda, Amazon SNS, and Amazon SQS using Python and Boto3.
