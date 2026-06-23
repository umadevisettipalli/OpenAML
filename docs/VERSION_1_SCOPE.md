# OpenAML Version 1 Scope

## Goal

Build a simple open-source AML analytics toolkit that can evaluate transaction data and generate alerts based on predefined AML monitoring scenarios.

## Target Users

* AML Analysts
* Compliance Teams
* FinTech Companies
* Students learning AML
* Data Analysts

## Input

The user uploads a CSV file containing transaction data.

## Output

The system generates:

* Alert report
* Alert explanations
* Summary statistics

## Supported Scenarios

### 1. Structuring Detection

Detect multiple transactions below a reporting threshold within a specified period.

### 2. High Velocity Detection

Detect unusually high numbers of transactions within a short timeframe.

### 3. Round Amount Detection

Detect repeated round-value transactions.

### 4. Dormant Account Reactivation

Detect significant activity after a long period of inactivity.

### 5. High Risk Geography Detection

Detect transactions involving high-risk jurisdictions.

## Out of Scope

* Real banking integrations
* Production transaction monitoring
* Customer onboarding
* Sanctions screening
* Case management workflows
* AI models

## Success Criteria

A user can upload sample transaction data and receive meaningful AML alerts with explanations.
