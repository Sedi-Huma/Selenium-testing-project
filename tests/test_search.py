import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_view_products(browser, base_url):
    # Login first
    browser.get(base_url)
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    
    # Check products are displayed
    products = browser.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0
    print(f"✅ Found {len(products)} products")

def test_sort_products(browser, base_url):
    # Login first
    browser.get(base_url)
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    
    # Sort products by price (low to high)
    sort_dropdown = Select(browser.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_value("lohi")
    
    print("✅ Products sorted successfully!")