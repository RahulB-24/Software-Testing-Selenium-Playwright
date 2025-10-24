from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://demoqa.com/automation-practice-form"

def test_registration_form():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(BASE_URL)
    driver.maximize_window()

    # Fill in form fields
    driver.find_element(By.ID, "firstName").send_keys("Test")
    driver.find_element(By.ID, "lastName").send_keys("User")
    driver.find_element(By.ID, "userEmail").send_keys("testuser@example.com")
    driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']").click()
    driver.find_element(By.ID, "userNumber").send_keys("9876543210")

    # Scroll to submit button and wait until clickable
    submit_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    submit_btn.click()

    # Wait for modal dialog to appear
    modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    )
    assert modal.is_displayed()

    driver.quit()
