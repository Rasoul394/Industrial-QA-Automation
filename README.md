# Industrial Monitoring QA Automation

## Project Overview
This project demonstrates automated testing for an industrial monitoring dashboard, inspired by my 13 years of experience in the steel industry (Isfahan Steel Company). 

The goal is to ensure that safety-critical systems, such as furnace temperature monitors, correctly display alarms when parameters exceed safety thresholds.

## Technical Stack
* **Language:** Python
* **Testing Framework:** PyTest
* **Automation Tool:** Selenium WebDriver
* **Design Pattern:** Functional Testing

## How it Works
The test script `test_industrial_dashboard.py` performs the following steps:
1. Launches a headless Chrome browser.
2. Loads the monitoring dashboard.
3. Validates that the temperature (1050°C) is correctly displayed.
4. Verifies that the status indicator shows **"Critical"**.
5. Confirms that the UI element has the correct CSS class (`text-danger`) for visual alerting.

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt