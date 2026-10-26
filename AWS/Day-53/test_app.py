
import unittest
from decimal import Decimal

from app import calculate_total_cost, check_budget


class TestCostMonitoring(unittest.TestCase):

    def test_total_cost(self):
        costs = [0.50, 1.25, 0.75]
        result = calculate_total_cost(costs)

        self.assertEqual(result, Decimal("2.50"))

    def test_within_budget(self):
        result = check_budget(1.50, 2.00)

        self.assertEqual(result, "WITHIN_BUDGET")

    def test_budget_exceeded(self):
        result = check_budget(3.00, 2.00)

        self.assertEqual(result, "ALERT")

    def test_equal_to_budget(self):
        result = check_budget(2.00, 2.00)

        self.assertEqual(result, "WITHIN_BUDGET")


if __name__ == "__main__":
    unittest.main()
