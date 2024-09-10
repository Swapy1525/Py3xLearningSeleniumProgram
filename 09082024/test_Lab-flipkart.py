from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Define the base URL
base_url = "https://www.flipkart.com"


# Function to close login popup if it appears
def close_login_popup():
    try:
        close_button = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
        close_button.click()
    except:
        print("Login popup did not appear.")


# Function to search for a product
def search_product(product_name):
    driver.get(base_url)
    close_login_popup()  # Close the login popup if it appears

    # Find the search bar and enter the product name
    search_bar = driver.find_element(By.NAME, "q")
    search_bar.send_keys(product_name)
    search_bar.send_keys(Keys.RETURN)

    # Wait for search results to load
    time.sleep(3)

    # Check if search results are displayed
    try:
        driver.find_element(By.CLASS_NAME, "_1YokD2")
        print(f"Search for {product_name} successful")
    except:
        print(f"No results found for {product_name}")


# Function to add the first product to the cart
def add_to_cart():
    try:
        first_product = driver.find_element(By.XPATH, "//div[@data-id]//a")
        first_product.click()
    except:
        print("Product not found in search results.")
        return

    # Switch to the new window that opens for the product details
    driver.switch_to.window(driver.window_handles[1])

    # Wait for the product page to load
    time.sleep(3)

    # Click the "Add to Cart" button
    try:
        add_to_cart_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Add to Cart')]")
        add_to_cart_btn.click()
        print("Product added to cart successfully")
    except:
        print("Failed to add product to cart")


# Function to proceed to checkout
def checkout():
    # Navigate to the cart page
    driver.get(f"{base_url}/viewcart?exploreMode=true&preference=cart")

    # Wait for the cart page to load
    time.sleep(3)

    # Click the "Place Order" button
    try:
        place_order_btn = driver.find_element(By.XPATH, "//span[text()='Place Order']")
        place_order_btn.click()
        print("Proceeding to checkout")
    except:
        print("Checkout process failed")


# Function to run the synthetic test
def run_synthetic_test(product_name):
    search_product(product_name)
    add_to_cart()
    checkout()


# Example usage
run_synthetic_test("iPhone 14")

# Close the browser after the test
driver.quit()
