
# Day 52 — Advanced AWS CloudFormation

## Project Overview

Implemented a reusable Infrastructure as Code (IaC) solution
using AWS CloudFormation and YAML.

Created and managed an Amazon S3 bucket through CloudFormation,
performed stack updates using Change Sets, detected configuration
drift, restored the expected configuration, and cleaned up
the deployed resources.

## AWS Services Used

- AWS CloudFormation
- Amazon S3
- AWS CLI
- AWS IAM

## Technologies

- YAML
- Windows PowerShell
- AWS CLI
- Visual Studio Code

## Project Structure

Day-52/
├── infrastructure.yaml
└── README.md

## CloudFormation Architecture

YAML Template
     |
     v
CloudFormation Stack
     |
     v
Amazon S3 Bucket
     |
     +--> Parameters
     +--> Resource Configuration
     +--> Outputs

## CloudFormation Components

### 1. Parameters

Parameters allow the same template to be reused across
different environments.

Our template supports:
- dev
- test
- prod

### 2. Resources

The Resources section defines the AWS infrastructure.

We created an S3 bucket with:
- Public access blocked
- Environment tags
- Project identification tags
- Versioning suspended

### 3. Outputs

Outputs return useful information after deployment.

Our template returns:
- S3 bucket name
- S3 bucket ARN
- Deployment environment

## Implementation

### Step 1 — Validate the Template

aws cloudformation validate-template \
  --template-body file://infrastructure.yaml \
  --region us-east-1

### Step 2 — Deploy the Stack

aws cloudformation deploy \
  --template-file infrastructure.yaml \
  --stack-name cloud-ai-day52-stack \
  --parameter-overrides EnvironmentName=dev \
  --region us-east-1

### Step 3 — Create a Change Set

Created a Change Set to update the environment parameter
from dev to test.

The proposed change modified the existing S3 bucket
without requiring resource replacement.

### Step 4 — Execute the Change Set

Applied the Change Set successfully.

Stack status: UPDATE_COMPLETE

### Step 5 — Detect Configuration Drift

Ran CloudFormation drift detection.

Initial result: IN_SYNC

Manually changed the S3 bucket's Environment tag
from test to production.

Second result: DRIFTED

Restored the tag to test.

Final result: IN_SYNC

### Step 6 — Delete Infrastructure

Deleted the CloudFormation stack using AWS CLI.

Verified that the temporary S3 bucket was removed.

## Important CloudFormation Commands

| Command | Purpose |
|---------|---------|
| validate-template | Validate template structure |
| deploy | Create or update infrastructure |
| describe-stacks | Retrieve stack information |
| create-change-set | Preview proposed changes |
| describe-change-set | Inspect proposed changes |
| execute-change-set | Apply approved changes |
| detect-stack-drift | Identify configuration differences |
| delete-stack | Remove managed infrastructure |

## Key Learnings

1. Infrastructure can be defined and managed using YAML.
2. Parameters make CloudFormation templates reusable.
3. Outputs expose useful deployment information.
4. Change Sets help preview infrastructure updates.
5. Stack updates can modify resources without replacement.
6. Drift detection identifies configuration differences.
7. Drift remediation restores the expected configuration.
8. CloudFormation manages the infrastructure lifecycle.

## Interview Takeaways

Q: What is Infrastructure as Code?
A: Managing infrastructure through machine-readable
configuration files rather than manual setup.

Q: What is a CloudFormation Change Set?
A: A preview of proposed stack changes before execution.

Q: What is configuration drift?
A: A difference between the expected infrastructure
configuration and the actual deployed configuration.

Q: Does CloudFormation automatically fix drift?
A: No. Drift detection identifies discrepancies,
but remediation must be performed separately.

Q: What happens when a CloudFormation stack is deleted?
A: CloudFormation attempts to delete its managed resources,
subject to resource dependencies and deletion policies.

## Conclusion

Successfully implemented a reusable AWS CloudFormation
template and practiced infrastructure deployment,
updates, Change Sets, drift detection, remediation,
and resource cleanup.
