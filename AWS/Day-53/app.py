
from decimal import Decimal


def calculate_total_cost(service_costs):
    """Calculate total AWS service spending."""
    return sum(
        (Decimal(str(cost)) for cost in service_costs),
        Decimal("0")
    )


def check_budget(total_cost, budget_limit):
    """Check whether spending exceeds the budget."""
    if Decimal(str(total_cost)) > Decimal(str(budget_limit)):
        return "ALERT"

    return "WITHIN_BUDGET"


if __name__ == "__main__":
    costs = [0.50, 1.25, 0.75]
    budget = 2.00

    total = calculate_total_cost(costs)
    status = check_budget(total, budget)

    print("AWS Cost Monitoring Application")
    print(f"Total Cost: ${total:.2f}")
    print(f"Budget Limit: ${budget:.2f}")
    print(f"Status: {status}")
