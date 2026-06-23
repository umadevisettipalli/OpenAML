# Structuring Detection Scenario

## Objective

Detect customers who perform multiple transactions below a reporting threshold within a defined time period.

## Example

Threshold: 10,000 USD

Transactions:

* 9,900
* 9,800
* 9,950
* 9,850
* 9,900

Individually these transactions appear normal.

Together they may indicate structuring behaviour.

## Initial Rule

Generate an alert when:

* Transaction amount is below 10,000
* At least 5 transactions occur
* Activity occurs within 7 days

## Alert Output

The alert should include:

* Customer ID
* Number of transactions
* Total amount
* Time period
* Alert reason

## Future Enhancements

* Dynamic thresholds
* Country-specific thresholds
* Risk-based thresholds
* Customer segmentation
