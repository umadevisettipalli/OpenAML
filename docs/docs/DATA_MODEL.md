# OpenAML Data Model

## Purpose

This document defines the minimum transaction data required for OpenAML Version 1.

OpenAML uses transaction data to detect basic AML monitoring scenarios and generate explainable alerts.

## Transaction Data

The input file should be named:

transactions.csv

## Required Columns

| Column Name | Description | Example |
|---|---|---|
| transaction_id | Unique ID for each transaction | TXN001 |
| customer_id | Unique ID for the customer | CUST001 |
| account_id | Unique ID for the account | ACC001 |
| transaction_date | Date of the transaction | 2026-06-23 |
| transaction_type | Credit or Debit | Credit |
| amount | Transaction amount | 9900 |
| currency | Transaction currency | USD |
| counterparty_country | Country linked to the transaction | UAE |
| channel | Transaction channel | Online |
| description | Short transaction description | Transfer received |

## Why These Columns Matter

These columns allow OpenAML to detect:

- Multiple transactions by the same customer
- Activity within a date range
- Round amount patterns
- High transaction volume
- High-risk geography activity

## Future Columns

Later versions may include:

- customer_risk_rating
- customer_country
- account_open_date
- customer_industry
- transaction_purpose
