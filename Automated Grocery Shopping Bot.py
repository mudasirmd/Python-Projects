from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# URL of the grocery store website
url = 'https://www.yourgrocerystore.com'

# User credentials for login (for security, you could use environment variables or a credentials manager)
username = 'myusername'
password = 'mypassword'

# List of items to purchase
shopping_list = ["bread", "milk", "eggs", "cheese", "butter"]

# Setup the webdriver (using Chrome)
# Specify the path to your chromedriver
chrome_driver_path = '/path/to/chromedriver'  # Replace with the actual path to your chromedriver

# Create a Service object
service = Service(chrome_driver_path)

# Initialize the WebDriver with the service
driver = webdriver.Chrome(service=service)

def login():
    driver.get(url)
    time.sleep(2)

    # Navigate to the login page
    login_button = driver.find_element(By.ID, "login_button")
    login_button.click()

    # Enter username and password
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys(username)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

def add_items_to_cart():
    # Iterate over the shopping list and add items to the cart
    for item in shopping_list:
        search_box = driver.find_element(By.ID, "search")
        search_box.send_keys(item)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        
        # Select the first result and add to cart
        add_to_cart_button = driver.find_element(By.CLASS_NAME, "add_to_cart")
        add_to_cart_button.click()
        time.sleep(2)

def checkout():
    # Navigate to the cart
    cart_button = driver.find_element(By.ID, "cart")
    cart_button.click()
    time.sleep(2)

    # Proceed to checkout
    checkout_button = driver.find_element(By.ID, "checkout_button")
    checkout_button.click()

    # Assuming there are some basic steps to fill for checkout like delivery address (could be automated if needed)
    time.sleep(3)

def main():
    login()
    add_items_to_cart()
    checkout()
    driver.quit()

if __name__ == "__main__":
    main()
