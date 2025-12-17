import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    """Create a Chrome browser for testing"""
    options = Options()
    options.add_argument("--headless")  # Run without opening window
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    
    yield driver  # This gives the driver to tests
    
    driver.quit()  # Close browser after test

@pytest.fixture
def base_url():
    """Return the base website URL"""
    return "https://www.saucedemo.com"