from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class QAJobsPage:
    def __init__(self, driver):
        """
        Initialize the QAJobsPage with a Selenium WebDriver instance
        and define all element locators.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Element locators
        self.SEE_ALL_JOBS_BUTTON = (By.XPATH, "//a[contains(text(), 'See all QA jobs')]")
        self.LOCATION_FILTER_BUTTON = (By.ID, "select2-filter-by-location-container")
        self.DEPARTMENT_FILTER_BUTTON = (By.ID, "select2-filter-by-department-container")
        self.LOCATION_OPTION = "//li[contains(text(), '{}')]"
        self.JOB_LIST = (By.CSS_SELECTOR, "div.job-list")
        self.JOB_POSITION = (By.CSS_SELECTOR, "span.position-department")
        self.JOB_LOCATION = (By.CSS_SELECTOR, "div.position-location")
        self.JOB_DEPARTMENT = (By.CSS_SELECTOR, "span.position-department") 
        self.JOB_CARDS = (By.CSS_SELECTOR, "div.position-list-item")
        self.SENIOR_POSITION = (By.XPATH, "//p[contains(text(), 'Senior Software Quality Assurance Engineer')]")
        self.VIEW_ROLE_BUTTONS = (By.CSS_SELECTOR, "a.btn.btn-navy")  # All 'View Role' buttons

    def click_see_all_qa_jobs(self):
        """Click the 'See all QA jobs' button to display the full QA job list."""
        print("Clicking 'See all QA jobs' button...")
        button = self.wait.until(EC.element_to_be_clickable(self.SEE_ALL_JOBS_BUTTON))
        button.click()
        print("'See all QA jobs' button clicked ✅")
        time.sleep(1)

    def filter_department(self, department_name):
        """Apply a department filter by selecting the desired department."""
        print(f"Applying department filter: {department_name}")
        self.wait.until(EC.element_to_be_clickable(self.DEPARTMENT_FILTER_BUTTON)).click()
        option = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.LOCATION_OPTION.format(department_name)))
        )
        option.click()
        print(f"Department filter applied: {department_name} ✅")
        time.sleep(1)

    def filter_location(self, location_name):
        """Apply a location filter by selecting the desired location."""
        print(f"Applying location filter: {location_name}")
        self.wait.until(EC.element_to_be_clickable(self.LOCATION_FILTER_BUTTON)).click()
        option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.LOCATION_OPTION.format(location_name)))
        )
        option.click()
        print(f"Location filter applied: {location_name} ✅")
        time.sleep(1)

    def scroll_job_list(self):
        """Scroll down the page slightly to make job cards visible."""
        print("Scrolling job list...")
        self.driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(2)
        print("Job list scrolled ✅")

    def is_senior_position_visible(self):
        """Verify if the Senior Software QA Engineer position is visible."""
        print("Checking visibility of Senior Software QA Engineer position...")
        visible = self.wait.until(
            EC.visibility_of_element_located(self.SENIOR_POSITION)
        ).is_displayed()
        print(f"Senior position visible: {visible}")
        return visible

    def validate_all_jobs(self, expected_position, expected_department, expected_location):
        """
        Validate that all job cards match the expected position, department, and location.
        Handles stale element references by re-fetching job cards each iteration.
        """
        print("Validating all QA job cards...")
        job_cards = self.wait.until(EC.presence_of_all_elements_located(self.JOB_CARDS))
        assert len(job_cards) > 0, "No job cards found!"
        print(f"Total job cards found: {len(job_cards)}")

        for index in range(len(job_cards)):
            # Re-fetch the job list each time to avoid stale element references
            job_cards = self.wait.until(EC.presence_of_all_elements_located(self.JOB_CARDS))
            job = job_cards[index]

            self.driver.execute_script("arguments[0].scrollIntoView(true);", job)
            time.sleep(0.5)

            position_department = job.find_element(By.CSS_SELECTOR, "span.position-department").text
            location = job.find_element(By.CSS_SELECTOR, "div.position-location").text

            print(f"Job {index+1}: {position_department} | {location}")

            assert expected_position in position_department, f"Position mismatch: {position_department}"
            assert expected_department in position_department, f"Department mismatch: {position_department}"
            assert expected_location in location, f"Location mismatch: {location}"

        print("All job cards validated ✅")

    def click_first_view_role_and_switch(self):
        """
        Hover over the first job card, click the 'View Role' button, 
        switch to the new tab, and verify the URL contains 'jobs.lever.co'.
        """
        print("Clicking first 'View Role' button and switching to new tab...")
        first_job_card = self.wait.until(
            EC.presence_of_all_elements_located(self.JOB_CARDS)
        )[0]

        actions = ActionChains(self.driver)
        actions.move_to_element(first_job_card).perform()
        print("Hovered over first job card ✅")

        first_view_role = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.position-list-item-wrapper a.btn.btn-navy"))
        )

        self.driver.execute_script("arguments[0].click();", first_view_role)
        print("'View Role' button clicked ✅")

        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(EC.url_contains("jobs.lever.co"))

        assert "jobs.lever.co" in self.driver.current_url
        print("Switched to Lever page tab and URL verified ✅")
