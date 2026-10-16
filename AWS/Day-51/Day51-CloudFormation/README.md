# Day 51 — Infrastructure as Code with CloudFormation

## Goal
Create and safely update AWS infrastructure using a YAML template.

## What I built
An encrypted SQS practice queue in us-east-1, managed by the
cloud-ai-journey-day51-practice CloudFormation stack.

## Files
- template.yaml: Defines the queue, settings, tags, and queue URL output.
- rules.guard: Requires every SQS queue to explicitly enable SQS-managed encryption.

## Workflow completed
1. Wrote the CloudFormation template.
2. Checked template syntax with AWS CLI.
3. Validated resource properties with cfn-lint.
4. Checked the encryption rule with CloudFormation Guard.
5. Reviewed a CREATE change set and deployed the stack.
6. Changed VisibilityTimeout from 30 to 60 seconds.
7. Reviewed an UPDATE change set confirming no queue replacement.
8. Applied the update and verified the actual SQS setting was 60.

## Key lessons
- A template describes the desired infrastructure.
- A stack groups the resources CloudFormation manages.
- A change set previews additions, modifications, and removals.
- Editing YAML does not change AWS until the update is deployed.
- Passing validation reduces errors but does not guarantee deployment success.

## Current status
Day 51 practice stack successfully deleted after verification.
Template and Guard rule retained for future deployments.
Day 50 cost-monitoring infrastructure remains active and unchanged.