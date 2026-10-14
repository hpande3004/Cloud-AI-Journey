
import boto3
import json
import os

from datetime import datetime, timezone
from decimal import Decimal

# AWS configuration
REGION = "us-east-1"

# Read configuration from environment variables
COST_THRESHOLD = Decimal(os.environ.get("COST_THRESHOLD_USD", "1.00"))
SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN")

# Initialize AWS clients
ce = boto3.client("ce", region_name=REGION)
sns = boto3.client("sns", region_name=REGION)


def get_monthly_cost():
    print("Retrieving AWS monthly spending...")

    today = datetime.now(timezone.utc).date()
    month_start = today.replace(day=1)

    # Cost Explorer end date is exclusive.
    # Query completed days in the current month.
    if today == month_start:
        return Decimal("0.00")

    response = ce.get_cost_and_usage(
        TimePeriod={
            "Start": month_start.isoformat(),
            "End": today.isoformat()
        },
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"]
    )

    total_cost = Decimal("0.00")

    for period in response.get("ResultsByTime", []):
        amount = period["Total"]["UnblendedCost"]["Amount"]
        total_cost += Decimal(amount)

    return total_cost


def send_cost_alert(total_cost):
    if not SNS_TOPIC_ARN:
        raise ValueError("SNS_TOPIC_ARN environment variable is missing")

    subject = "AWS Cost Alert - Threshold Exceeded"

    message = (
        "AWS Cost Monitoring Alert\n\n"
        f"Current Month Cost: ${total_cost:.2f}\n"
        f"Configured Threshold: ${COST_THRESHOLD:.2f}\n\n"
        "Please review your AWS billing dashboard."
    )

    response = sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=subject,
        Message=message
    )

    print("SNS alert published successfully!")
    print("Message ID:", response["MessageId"])


def lambda_handler(event, context):
    print("Starting AWS Cost Monitoring...")

    total_cost = get_monthly_cost()

    print(f"Current Month Cost: ${total_cost:.2f}")
    print(f"Cost Threshold: ${COST_THRESHOLD:.2f}")

    alert_sent = False

    if total_cost > COST_THRESHOLD:
        print("Cost threshold exceeded!")
        send_cost_alert(total_cost)
        alert_sent = True
    else:
        print("AWS spending is within the configured threshold.")

    result = {
        "MonthlyCostUSD": str(total_cost),
        "ThresholdUSD": str(COST_THRESHOLD),
        "AlertSent": alert_sent
    }

    print("Cost monitoring completed successfully!")

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }


# Run locally for testing
if __name__ == "__main__":
    lambda_handler({}, None)
