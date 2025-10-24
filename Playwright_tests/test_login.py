from playwright.sync_api import sync_playwright

BASE_URL = "https://the-internet.herokuapp.com/login"

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(BASE_URL)

        page.fill("#username", "tomsmith")
        page.fill("#password", "SuperSecretPassword!")
        page.click("button[type='submit']")

        page.wait_for_load_state("networkidle")
        assert "/secure" in page.url
        browser.close()

def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(BASE_URL)

        page.fill("#username", "wronguser")
        page.fill("#password", "wrongpass")
        page.click("button[type='submit']")

        error = page.locator("#flash")
        assert "Your username is invalid!" in error.text_content()
        browser.close()
