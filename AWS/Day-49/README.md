
# Day 49 - Automated AWS Resource Monitoring

## Project Overview

Built a scheduled, serverless AWS resource monitoring system using Python, Boto3, AWS Lambda, Amazon EventBridge Scheduler, and Amazon CloudWatch.

The application automatically retrieves information about EC2 instances and S3 buckets at scheduled intervals.

## AWS Services Used

- Amazon EventBridge Scheduler - Scheduled automation
- AWS Lambda - Serverless Python execution
- Amazon EC2 - Instance inventory and status
- Amazon S3 - Bucket inventory
- Amazon CloudWatch - Execution logs and monitoring
- AWS IAM - Access and permission management

## Technologies

- Python 3.14
- Boto3
- AWS Management Console
- AWS CLI
- Git and GitHub

## Architecture

EventBridge Scheduler
        |
        | Every 5 minutes
        v
    AWS Lambda
        |
        | Python + Boto3
        |
        +----> Amazon EC2
        |      Describe Instances
        |
        +----> Amazon S3
        |      List Buckets
        |
        v
  CloudWatch Logs

## Project Structure

Day-49/
|
|-- AWS_Resource_Monitor.py
|-- README.md

## Features

- Automatically invokes AWS Lambda on a schedule
- Retrieves EC2 instance IDs and their states
- Lists existing S3 buckets
- Supports paginated EC2 API responses
- Logs monitoring results to CloudWatch
- Runs without requiring a local computer
- Uses read-only IAM permissions

## Implementation Steps

1. Developed the Python monitoring script using Boto3.
2. Tested the script locally.
3. Created an AWS Lambda function.
4. Configured the Lambda execution role.
5. Granted EC2 and S3 read permissions.
6. Deployed the Python script to Lambda.
7. Tested Lambda execution manually.
8. Created an EventBridge Scheduler schedule.
9. Configured automatic execution every five minutes.
10. Verified scheduled executions in CloudWatch Logs.

## Lambda Configuration

Function name:
cloud-ai-day49-resource-monitor

Runtime:
Python 3.14

Handler:
lambda_function.lambda_handler

Region:
us-east-1

## IAM Permissions

The Lambda execution role requires:

- ec2:DescribeInstances
- s3:ListAllMyBuckets
- CloudWatch Logs permissions

The EventBridge Scheduler execution role requires permission to invoke the Lambda function.

## EventBridge Configuration

Schedule name:
cloud-ai-day49-monitor-schedule

Schedule expression:
rate(5 minutes)

Schedule type:
Recurring

Flexible time window:
Off

Target:
AWS Lambda

## Testing

### Local Testing

Run:

    python AWS_Resource_Monitor.py

### Lambda Testing

Invoke the Lambda function with an empty JSON event:

    {}

### Scheduled Testing

Enable the EventBridge schedule and inspect CloudWatch Logs.

Expected results:

- Lambda executes automatically.
- EC2 instance information is retrieved.
- S3 bucket names are retrieved.
- Execution results are logged to CloudWatch.
- New invocations occur approximately every five minutes.

## Key Learnings

### Scheduled Automation

EventBridge Scheduler invokes AWS services according to a configured schedule.

### Serverless Computing

AWS Lambda executes Python code without requiring server management.

### Boto3

Boto3 allows Python applications to interact with AWS services programmatically.

### IAM Roles

Lambda and EventBridge Scheduler use separate IAM execution roles.

### CloudWatch Logs

CloudWatch records execution details and helps troubleshoot failures.

### Pagination

Boto3 paginators retrieve multiple pages of AWS API results.

## Cleanup

After testing, delete the temporary AWS resources:

- EventBridge schedule
- Lambda function
- Project-specific IAM roles and policies
- Lambda CloudWatch log group

## Conclusion

Successfully implemented an automated AWS resource monitoring system using EventBridge Scheduler, Lambda, Python, and Boto3.

The project demonstrates scheduled serverless automation and AWS infrastructure monitoring.
