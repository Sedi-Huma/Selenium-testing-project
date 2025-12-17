import pytest
from selenium.webdriver.common.by import By

def test_valid_login(browser, base_url):
    # Go to website
    browser.get(base_url)
    
    # Find login elements
    username = browser.find_element(By.ID, "user-name")
    password = browser.find_element(By.ID, "password")
    login_btn = browser.find_element(By.ID, "login-button")
    
    # Enter credentials
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_btn.click()
    
    # Verify login successful
    assert "inventory" in browser.current_url
    print("✅ Login successful!")

def test_invalid_login(browser, base_url):
    # Go to website
    browser.get(base_url)
    
    # Find login elements
    username = browser.find_element(By.ID, "user-name")
    password = browser.find_element(By.ID, "password")
    login_btn = browser.find_element(By.ID, "login-button")
    
    # Enter WRONG credentials
    username.send_keys("wrong_user")
    password.send_keys("wrong_password")
    login_btn.click()
    
    # Verify error message shows
    error = browser.find_element(By.CLASS_NAME, "error-message-container")
    assert error.is_displayed()
    print("✅ Invalid login error shown!")