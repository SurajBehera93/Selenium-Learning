# Importing the 'time' module for adding delays
import time

# Importing necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Creating Chrome options
chrome_options = Options()

# Adding experimental option to detach the browser window
chrome_options.add_experimental_option("detach", True)

# Creating a service object for the Chrome browser/used to start and stop driver
service_obj = Service()

# Creating a Chrome webdriver instance with the specified service and options
# Here we have created object from webdriver class to access methods present in the class
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.maximize_window()#maximizes driver window

# Called the get method from webdriver class using the driver object
driver.get("https://rahulshettyacademy.com/client/")


print(driver.__getattribute__("title"))
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("demo@gmail.com")
driver.find_element(By.XPATH, "//input[@type='email']").clear()
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("demo@gmail.com")
driver.find_element(By.XPATH, "//input[@id='userPassword']").send_keys("123456")
driver.find_element(By.XPATH, "//input[@id='confirmPassword']").send_keys("123456")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
