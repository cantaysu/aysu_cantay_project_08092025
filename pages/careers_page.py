# pages/careers_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CareersPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

        # -------------------
        # Element locators
        # -------------------
        self.SEE_ALL_TEAMS = (By.XPATH, "//a[text()='See all teams']")
        self.FINANCE_TEAM = (By.XPATH, "//h3[text()='Finance & Business Support']")
        self.MARKETING_TEAM = (By.XPATH, "//h3[text()='Marketing']")
        self.CEO_TEAM = (By.XPATH, "//h3[text()='CEO’s Executive Office']")
        self.LOCATIONS_TITLE = (By.XPATH, "//h3[contains(text(),'Our Locations')]")
        self.LOCATIONS_DESC = (By.XPATH, "//p[contains(text(),'28 offices across 6 continents')]")
        self.LIFE_AT_INSIDER = (By.XPATH, "//h2[text()='Life at Insider']")
        self.QA_TEAM = (By.XPATH, "//h3[text()='Quality Assurance']")

    # -------------------
    # Helper Methods
    # -------------------

    def scroll_to_element(self, element_locator):
        """Scroll the page to make the element visible in the viewport"""
        element = self.wait.until(EC.presence_of_element_located(element_locator))
        self.actions.move_to_element(element).perform()
        print(f"Scrolled to element: {element_locator}")

    # -------------------
    # Team Section Methods
    # -------------------

    def click_see_all_teams(self):
        """Scroll to 'See all teams' and click the link"""
        print("Clicking 'See all teams'...")
        self.scroll_to_element(self.SEE_ALL_TEAMS)
        self.wait.until(EC.element_to_be_clickable(self.SEE_ALL_TEAMS)).click()
        print("'See all teams' clicked ✅")

    def is_finance_visible(self):
        """Check if Finance team section is visible"""
        print("Checking Finance team visibility...")
        self.scroll_to_element(self.FINANCE_TEAM)
        visible = self.wait.until(EC.visibility_of_element_located(self.FINANCE_TEAM)).is_displayed()
        print(f"Finance team visible: {visible}")
        return visible

    def is_marketing_visible(self):
        """Check if Marketing team section is visible"""
        print("Checking Marketing team visibility...")
        self.scroll_to_element(self.MARKETING_TEAM)
        visible = self.wait.until(EC.visibility_of_element_located(self.MARKETING_TEAM)).is_displayed()
        print(f"Marketing team visible: {visible}")
        return visible

    def is_ceo_visible(self):
        """Check if CEO’s Executive Office section is visible"""
        print("Checking CEO team visibility...")
        self.scroll_to_element(self.CEO_TEAM)
        visible = self.wait.until(EC.visibility_of_element_located(self.CEO_TEAM)).is_displayed()
        print(f"CEO team visible: {visible}")
        return visible

    # -------------------
    # Locations Section Methods
    # -------------------

    def is_locations_visible(self):
        """Check if Locations title is visible"""
        print("Checking Locations title visibility...")
        self.scroll_to_element(self.LOCATIONS_TITLE)
        visible = self.wait.until(EC.visibility_of_element_located(self.LOCATIONS_TITLE)).is_displayed()
        print(f"Locations title visible: {visible}")
        return visible

    def is_locations_desc_visible(self):
        """Check if Locations description is visible"""
        print("Checking Locations description visibility...")
        visible = self.wait.until(EC.visibility_of_element_located(self.LOCATIONS_DESC)).is_displayed()
        print(f"Locations description visible: {visible}")
        return visible

    # -------------------
    # Life at Insider Section Methods
    # -------------------

    def is_life_visible(self):
        """Check if 'Life at Insider' section is visible"""
        print("Checking 'Life at Insider' section visibility...")
        self.scroll_to_element(self.LIFE_AT_INSIDER)
        visible = self.wait.until(EC.visibility_of_element_located(self.LIFE_AT_INSIDER)).is_displayed()
        print(f"'Life at Insider' section visible: {visible}")
        return visible

    # -------------------
    # QA Team Section Methods
    # -------------------

    def click_qa_team(self):
        """Scroll to QA team section and click it"""
        print("Clicking QA team section...")
        qa = self.wait.until(EC.presence_of_element_located(self.QA_TEAM))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", qa)
        self.wait.until(EC.element_to_be_clickable(self.QA_TEAM))
        self.driver.execute_script("arguments[0].click();", qa)
        print("QA team section clicked ✅")
