# Industrial Monitoring System - Automation Test Suite

## Project Description
This repository contains an automated functional test suite for a web-based industrial monitoring dashboard. The project simulates a real-world scenario where sensor data (like temperature and pressure) must be monitored, and safety alerts must be validated automatically.

## Purpose
The main goal is to ensure that the monitoring software correctly identifies critical system states and triggers the appropriate UI alerts (e.g., color changes and status updates) when safety thresholds are exceeded.

## Tech Stack
* **Language:** Python 3.x
* **Framework:** PyTest
* **Tool:** Selenium WebDriver
* **Architecture:** Functional Testing with Automated Assertions

## Test Scenarios Covered
1. **Dashboard Loading:** Verifies the monitoring page opens correctly.
2. **Threshold Validation:** Checks if specific temperature values are displayed accurately.
3. **Alarm Triggering:** Validates that the "Critical" status and red alert CSS classes are applied when the temperature exceeds 1000°C.

## Installation & Execution
1. Clone the repository.
2. Install required packages:
   ```bash
   pip install -r requirements.txt