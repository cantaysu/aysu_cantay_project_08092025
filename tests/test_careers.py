import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_page import QAJobsPage
import time

# -------------------
# Scenario 1: Insider home page open check
# -------------------
def test_home_page_opens(driver):
    print("\n=== Scenario 1: Home page open check ===")
    home = HomePage(driver)
    
    print("Opening Insider home page...")
    home.open()
    
    print("Declining cookies if present...")
    home.decline_cookies_if_present()
    
    print("Checking if logo is visible...")
    if home.is_logo_visible():
        print("Insider logo is visible.")
    else:
        print("Insider logo is NOT visible.")
        assert False, "Insider home page logo is not visible!"
    
    print("Scenario 1 completed.\n")

# -------------------
# Scenario 2: Careers visibility
# -------------------
def test_careers_visibility(driver):
    print("\n=== Scenario 2: Careers visibility ===")
    home = HomePage(driver)
    
    print("Opening Insider home page...")
    home.open()
    print("Declining cookies if present...")
    home.decline_cookies_if_present()
    
    print("Navigating to Careers page...")
    home.go_to_careers()
    
    careers = CareersPage(driver)
    print("Clicking 'See all teams'...")
    careers.click_see_all_teams()
    
    print("Checking visibility of Finance team...")
    assert careers.is_finance_visible()
    print("Finance team is visible.")
    
    print("Checking visibility of Marketing team...")
    assert careers.is_marketing_visible()
    print("Marketing team is visible.")
    
    print("Checking visibility of CEO team...")
    assert careers.is_ceo_visible()
    print("CEO team is visible.")
    
    print("Checking visibility of Locations section...")
    assert careers.is_locations_visible()
    print("Locations title is visible.")
    
    assert careers.is_locations_desc_visible()
    print("Locations description is visible.")
    
    print("Checking visibility of 'Life at Insider' section...")
    assert careers.is_life_visible()
    print("'Life at Insider' section is visible.")
    
    print("Scenario 2 completed.\n")

# -------------------
# Scenario 3: QA jobs filters
# -------------------
def test_qa_jobs_filters(driver):
    print("\n=== Scenario 3: QA jobs filters ===")
    home = HomePage(driver)
    
    print("Opening Insider home page...")
    home.open()
    print("Declining cookies if present...")
    home.decline_cookies_if_present()
    
    print("Navigating to Careers page...")
    home.go_to_careers()
    
    careers = CareersPage(driver)
    print("Clicking 'See all teams'...")
    careers.click_see_all_teams()
    print("Clicking QA team...")
    careers.click_qa_team()
    
    qa_page = QAJobsPage(driver)
    print("Clicking 'See all QA jobs'...")
    qa_page.click_see_all_qa_jobs()
    
    print("Waiting for job list to load...")
    time.sleep(10)
    
    print("Filtering by location: Istanbul, Turkiye")
    qa_page.filter_location("Istanbul, Turkiye")
    print("Filtering by department: Quality Assurance")
    qa_page.filter_department("Quality Assurance")
    
    print("Scrolling job list...")
    qa_page.scroll_job_list()
    
    print("Checking if Senior Software QA Engineer is visible...")
    assert qa_page.is_senior_position_visible()
    print("Senior Software QA Engineer position is visible.")
    
    print("Scenario 3 completed.\n")

# -------------------
# Scenario 4: Validate all job listings
# -------------------
def test_validate_all_jobs(driver):
    print("\n=== Scenario 4: Validate all job listings ===")
    home = HomePage(driver)
    
    print("Opening Insider home page...")
    home.open()
    print("Declining cookies if present...")
    home.decline_cookies_if_present()
    print("Navigating to Careers page...")
    home.go_to_careers()
    
    careers = CareersPage(driver)
    print("Clicking 'See all teams'...")
    careers.click_see_all_teams()
    print("Clicking QA team...")
    careers.click_qa_team()
    
    qa_page = QAJobsPage(driver)
    print("Clicking 'See all QA jobs'...")
    qa_page.click_see_all_qa_jobs()
    
    print("Waiting for job list to load...")
    time.sleep(10)
    
    print("Applying filters: Department=Quality Assurance, Location=Istanbul, Turkiye")
    qa_page.filter_department("Quality Assurance")
    qa_page.filter_location("Istanbul, Turkiye")
    
    print("Validating all job cards match expected filters...")
    qa_page.validate_all_jobs(
        expected_position="Quality Assurance",
        expected_department="Quality Assurance",
        expected_location="Istanbul, Turkiye"
    )
    print("All job cards match the expected filters.")
    
    print("Scenario 4 completed.\n")

# -------------------
# Scenario 5: View Role button redirects to Lever
# -------------------
def test_view_role_redirects_to_lever(driver):
    print("\n=== Scenario 5: View Role button redirects to Lever ===")
    home = HomePage(driver)
    
    print("Opening Insider home page...")
    home.open()
    print("Declining cookies if present...")
    home.decline_cookies_if_present()
    print("Navigating to Careers page...")
    home.go_to_careers()
    
    careers = CareersPage(driver)
    print("Clicking 'See all teams'...")
    careers.click_see_all_teams()
    print("Clicking QA team...")
    careers.click_qa_team()
    
    qa_page = QAJobsPage(driver)
    print("Clicking 'See all QA jobs'...")
    qa_page.click_see_all_qa_jobs()
    
    print("Waiting for job list to load...")
    time.sleep(10)
    
    print("Applying filters: Location=Istanbul, Turkiye, Department=Quality Assurance")
    qa_page.filter_location("Istanbul, Turkiye")
    qa_page.filter_department("Quality Assurance")
    
    print("Clicking first 'View Role' button and switching to new tab...")
    qa_page.click_first_view_role_and_switch()
    print("New tab opened and URL contains 'jobs.lever.co'.")
    
    print("Scenario 5 completed.\n")
