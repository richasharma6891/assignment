# First Test Case
#------------
# Project Overview:
# Our project is a Pathology Lab Management web application
# that helps manage various aspects of a pathology lab.
# The application features the following key components:

#1. Login Page:
#URL: https://gor-pathology.web.app/
#Credentials:
#- Username: test@kennect.io
#- Password: Qwerty@1234

#2. Home Page:
#After successful login, the user will land on the home page
# where they can view a list of todos and access the Cost Calculator for blood tests.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('C:\\Drivers\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://gor-pathology.web.app/")
driver.maximize_window()

driver.find_element(By.NAME,"email").send_keys("test@kennect.io")
driver.find_element(By.NAME, "password").send_keys("Qwerty@1234")
driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME,"MuiButton-label").click()

act_title = driver.title
exp_title = "Dashboard"

if act_title == exp_title:
    print("Login test Passed")
else:
    print("Login test Failed")

driver.quit()