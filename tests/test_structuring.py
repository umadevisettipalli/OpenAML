from openaml.scenarios.structuring import StructuringDetector


def test_structuring_detector_creates_alert():
    transactions = [
        {"customer_id": "CUST001", "amount": 9900},
        {"customer_id": "CUST001", "amount": 9800},
        {"customer_id": "CUST001", "amount": 9950},
        {"customer_id": "CUST001", "amount": 9850},
        {"customer_id": "CUST001", "amount": 9900},
    ]

    detector = StructuringDetector()
    alerts = detector.detect(transactions)

    assert len(alerts) == 1
    assert alerts[0]["customer_id"] == "CUST001"
    assert alerts[0]["scenario"] == "Structuring Detection"
