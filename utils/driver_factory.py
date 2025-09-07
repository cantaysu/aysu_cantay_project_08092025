from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    """
    Initialize and return a Selenium Chrome WebDriver instance.

    Features:
    - Uses webdriver_manager to automatically manage ChromeDriver installation.
    - Starts Chrome in maximized window mode.
    - Returns the driver object ready to use in tests.
    """
    # Configure Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Start browser maximized for better visibility

    # Automatically download and configure ChromeDriver using webdriver_manager
    service = Service(ChromeDriverManager().install())

    # Initialize Chrome WebDriver with the service and options
    driver = webdriver.Chrome(service=service, options=options)

    return driver
