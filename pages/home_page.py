# pages/home_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    URL = "https://useinsider.com/"

    COOKIE_DECLINE_BTN = (By.ID, "wt-cli-reject-btn")
    COMPANY_MENU = (By.XPATH, "//a[contains(text(),'Company')]")
    CAREERS_LINK = (By.XPATH, "//a[contains(text(),'Careers')]")
    INSIDER_LOGO = (By.CSS_SELECTOR, "img[alt='insider_logo']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Open Insider homepage"""
        self.driver.get(self.URL)
        print("Opened Insider homepage")

    def decline_cookies_if_present(self):
        """Click 'Decline' button if cookies popup appears"""
        try:
            decline_btn = self.wait.until(EC.element_to_be_clickable(self.COOKIE_DECLINE_BTN))
            decline_btn.click()
            print("Cookies declined")
        except:
            print("No cookies popup found")

    def go_to_careers(self):
        """Navigate to Careers page via Company menu"""
        company = self.wait.until(EC.element_to_be_clickable(self.COMPANY_MENU))
        company.click()
        print("Clicked Company menu")
        careers = self.wait.until(EC.element_to_be_clickable(self.CAREERS_LINK))
        careers.click()
        print("Clicked Careers link")

    def is_logo_visible(self):
        """Check if the Insider logo is visible on the page"""
        logo = self.wait.until(EC.visibility_of_element_located(self.INSIDER_LOGO))
        if logo.is_displayed():
            print("Insider logo is visible")
        else:
            print("Insider logo is NOT visible")
        return logo.is_displayed()
