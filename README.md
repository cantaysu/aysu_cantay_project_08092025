QA Automation Tests

This repository contains Selenium-based automated tests for Insider's website, focusing on the Careers section and Quality Assurance job listings. The tests are written in Python using the Page Object Model (POM) for better maintainability and readability.

Setup Instructions:

1. Clone the repository:
   git clone https://github.com/cantaysu/aysu_cantay_project_08092025.git

2. Navigate to the project directory:
   cd aysu_cantay_project_08092025

3. Create and activate a virtual environment (recommended):
   python3 -m venv venv
   source venv/bin/activate   (macOS/Linux)
   venv\Scripts\activate      (Windows)

4. Install dependencies:
   pip install -r requirements.txt

5. Run the tests:
   pytest -v tests/

Project Overview:

- tests/test_careers.py: Contains all the test scenarios for Insider's homepage, Careers page, QA team filters, job validation, and View Role button.
- pages/home_page.py: Page object for the Insider home page.
- pages/careers_page.py: Page object for the Careers page.
- pages/qa_page.py: Page object for the QA Jobs page.
- requirements.txt: Lists all Python dependencies.

Test Scenarios:

1. Verify the Insider homepage opens and the logo is visible.
2. Navigate to the Careers page and check visibility of Teams, Locations, and Life at Insider sections.
3. Navigate to the QA team page, apply filters (Location: Istanbul, Turkey, Department: Quality Assurance), and verify job list presence.
4. Validate that all job listings contain the correct Position, Department, and Location.
5. Click the 'View Role' button and verify redirection to the Lever application page.

Notes:

- The tests use Selenium WebDriver with Chrome.
- The Page Object Model (POM) is implemented to separate page interactions from test logic.
- Assertions are used to ensure correctness.
- No BDD frameworks are used.
- Optimized XPath and CSS selectors are applied for buttons, dropdowns, and other elements.

Usage:

After cloning and installing dependencies, you can run all tests using:
pytest -v tests/

The console will display detailed step-by-step logs of each scenario.
