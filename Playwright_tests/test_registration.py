from playwright.sync_api import sync_playwright

BASE_URL = "https://demoqa.com/automation-practice-form"

def test_registration_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(BASE_URL)
        page.set_viewport_size({"width": 1200, "height": 800})

        # Fill in form fields
        page.fill("#firstName", "Test")
        page.fill("#lastName", "User")
        page.fill("#userEmail", "testuser@example.com")
        page.click("label[for='gender-radio-1']")
        page.fill("#userNumber", "9876543210")

        # Scroll to submit button and click
        page.locator("#submit").scroll_into_view_if_needed()
        page.locator("#submit").click()

        # Wait for modal dialog to appear
        modal = page.locator("#example-modal-sizes-title-lg")
        modal.wait_for(state="visible", timeout=5000)
        assert modal.is_visible()

        browser.close()
