from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Set up the WebDriver using webdriver_manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Step 1: Open the website
    driver.get("https://www.saucedemo.com/")
    print("Opened the website")

    # Step 2: Log in with valid credentials
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username.send_keys("standard_user")  # Valid username
    password.send_keys("secret_sauce")   # Valid password
    login_button.click()
    print("Logged in successfully")

    # Step 3: Verify login is successful by checking the URL
    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))
    assert "inventory.html" in driver.current_url, "Login failed! Not redirected to the inventory page."
    print("Login verified: Redirected to the inventory page")

    # Step 4: Add a product to the cart
    add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_button.click()
    print("Added product to the cart")

    # Step 5: Verify the product is added to the cart
    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
    cart_item = driver.find_element(By.CLASS_NAME, "cart_item")
    assert cart_item.is_displayed(), "Product not added to the cart!"
    print("Product verified in the cart")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
    print("Browser closed")