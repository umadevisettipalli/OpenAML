"""
Structuring Detection Scenario

This module detects customers who perform multiple transactions
below a reporting threshold within a defined time period.
"""


class StructuringDetector:
    """
    Detects possible structuring activity in transaction data.
    """

    def __init__(self, threshold=10000, minimum_transactions=5):
        self.threshold = threshold
        self.minimum_transactions = minimum_transactions

    def detect(self, transactions):
        """
        Detect structuring activity.

        Args:
            transactions: A list of transaction dictionaries.

        Returns:
            A list of alert dictionaries.
        """
        alerts = []

        customer_transactions = {}

        for transaction in transactions:
            customer_id = transaction["customer_id"]
            amount = float(transaction["amount"])

            if amount < self.threshold:
                if customer_id not in customer_transactions:
                    customer_transactions[customer_id] = []

                customer_transactions[customer_id].append(transaction)

        for customer_id, grouped_transactions in customer_transactions.items():
            if len(grouped_transactions) >= self.minimum_transactions:
                total_amount = sum(float(txn["amount"]) for txn in grouped_transactions)

                alert = {
                    "customer_id": customer_id,
                    "scenario": "Structuring Detection",
                    "transaction_count": len(grouped_transactions),
                    "total_amount": total_amount,
                    "reason": "Multiple transactions below reporting threshold detected.",
                }

                alerts.append(alert)

        return alerts
