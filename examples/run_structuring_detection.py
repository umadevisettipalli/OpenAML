from openaml.scenarios.structuring import StructuringDetector

transactions = [
    {"customer_id": "CUST001", "amount": 9900},
    {"customer_id": "CUST001", "amount": 9800},
    {"customer_id": "CUST001", "amount": 9950},
    {"customer_id": "CUST001", "amount": 9850},
    {"customer_id": "CUST001", "amount": 9900},
]

detector = StructuringDetector()
alerts = detector.detect(transactions)

print(alerts)
