import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os


# Fixture to initialize and close the browser
@pytest.fixture
def browser_setup():
    # Setup Chrome Driver automatically
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Runs browser in background
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


# Test case for checking the furnace temperature alarm
def test_furnace_temperature_alarm(browser_setup):
    driver = browser_setup

    # 1. Load the monitoring dashboard
    # Finding the path of the HTML file we created
    file_path = os.path.abspath("dashboard_mock.html")
    driver.get(f"file://{file_path}")

    # 2. Locate the temperature and status elements
    temp_element = driver.find_element(By.ID, "temp-value")
    status_element = driver.find_element(By.ID, "status-indicator")

    # 3. Extract values for validation
    current_temp = temp_element.text
    current_status = status_element.text

    # 4. Assertions (The core of the test)
    # Check if the temperature value is displayed correctly
    assert "1050" in current_temp

    # Check if the status is 'Critical' for high temperatures
    assert "Critical" in current_status

    # Check if the alarm color is red (Bootstrap 'text-danger' class)
    assert "text-danger" in status_element.get_attribute("class")

    print(f"\nTest Passed: Temperature is {current_temp}°C and Status is {current_status}.")