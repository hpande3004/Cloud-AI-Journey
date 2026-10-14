
# Day 50 — AWS Cost Monitoring & Budget Alerts Using Python

## Project Overview

Built an automated AWS cost monitoring system using Python,
AWS Lambda, Cost Explorer, Amazon SNS, EventBridge Scheduler,
and CloudWatch Logs.

The system retrieves monthly AWS spending, compares it against
a configurable threshold, and sends an email notification when
the threshold is exceeded.

## AWS Services Used

| Service | Purpose |
|---------|---------|
| AWS Cost Explorer | Retrieve billing information |
| AWS Lambda | Execute Python monitoring logic |
| Amazon SNS | Send email notifications |
| EventBridge Scheduler | Trigger Lambda daily |
| Amazon CloudWatch | Store execution logs |
| AWS IAM | Manage service permissions |

## Architecture

EventBridge Scheduler (Every 24 Hours)
             |
             v
         AWS Lambda
             |
             v
      AWS Cost Explorer
             |
             v
     Compare with Threshold
             |
       +-----+-----+
       |           |
   Cost <= $1   Cost > $1
       |           |
    No Alert    Amazon SNS
                   |
                   v
             Email Notification

CloudWatch Logs records Lambda execution details.

## Python Implementation

File: `AWS_Cost_Monitor.py`

### Key Operations

1. Initialize Boto3 clients for Cost Explorer and SNS.
2. Calculate the current month's billing period.
3. Retrieve monthly unblended AWS costs.
4. Compare spending against the configured threshold.
5. Publish an SNS notification if the threshold is exceeded.
6. Return execution results and write logs.

### Important Boto3 Methods

- `boto3.client("ce")`
- `ce.get_cost_and_usage()`
- `boto3.client("sns")`
- `sns.publish()`

## Environment Variables

| Variable | Purpose |
|----------|---------|
| COST_THRESHOLD_USD | Alert threshold in USD |
| SNS_TOPIC_ARN | SNS topic for notifications |

Example threshold: $1.00

## Lambda Configuration

Function: `cloud-ai-day50-cost-monitor`

Runtime: Python 3.14

Handler: `lambda_function.lambda_handler`

Timeout: 30 seconds

IAM permissions:
- ce:GetCostAndUsage
- sns:Publish
- AWSLambdaBasicExecutionRole

## EventBridge Configuration

Schedule: `cloud-ai-day50-daily-cost-monitor`

Expression: `rate(1 day)`

Target: AWS Lambda function

Status: Enabled

## Testing

### Local Python Test

Executed the monitoring script using AWS credentials.

Result:
- Cost Explorer API request succeeded.
- Reported monthly spending: $0.00
- Configured threshold: $1.00
- No cost alert required.

### AWS Lambda Test

Invoked the Lambda function manually and verified
the execution results using CloudWatch Logs.

### Amazon SNS Test

Published a test message directly to the SNS topic
and successfully received an email notification.

### EventBridge Scheduler

Configured and enabled the daily Lambda invocation
schedule.

Automatic execution can be verified after the
first scheduled invocation.

## Key Learnings

- AWS billing information can be accessed using Boto3.
- Lambda can execute Python scripts without a local server.
- Environment variables make application configuration flexible.
- SNS can deliver automated email notifications.
- EventBridge Scheduler enables recurring cloud automation.
- IAM execution roles provide AWS service permissions.
- CloudWatch Logs helps monitor and troubleshoot execution.

## Limitations

- Cost Explorer billing information is not real-time.
- The script queries completed days of the current month.
- Alerts are sent only when spending exceeds the threshold.
- Alerts may repeat on subsequent daily executions.
- This custom monitoring system does not enforce a spending cap.
- AWS services and Cost Explorer API requests may incur charges.

## Conclusion

Successfully developed and deployed an automated AWS
cost monitoring solution using Python and serverless
AWS services.
