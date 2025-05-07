from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager

ACCOUNT_EMAIL = "YOUR LOGIN EMAIL"
ACCOUNT_PASSWORD = "YOUR LOGIN PASSWORD"
PHONE = "YOUR PHONE NUMBER"

def abort_application():
    try:
        driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()
        time.sleep(2)
        driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1].click()
    except NoSuchElementException:
        pass

chrome_driver_path = ChromeDriverManager().install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ChromeService(executable_path=chrome_driver_path), options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3586148395&f_LF=f_AL&geoId=101356765&keywords=python&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")

# Reject Cookies
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'button[action-type="DENY"]').click()

# Sign in
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Sign in").click()
time.sleep(5)
driver.find_element(By.ID, "username").send_keys(ACCOUNT_EMAIL)
driver.find_element(By.ID, "password").send_keys(ACCOUNT_PASSWORD, Keys.ENTER)

input("Press Enter when you have solved the Captcha")

# Job Applications
time.sleep(5)
for listing in driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable"):
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button").click()
        time.sleep(5)
        phone_field = driver.find_element(By.CSS_SELECTOR, "input[id*=phoneNumber]")
        if not phone_field.get_attribute("value"):
            phone_field.send_keys(PHONE)
        
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        
        print("Submitting job application")
        submit_button.click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()
    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
