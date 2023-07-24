import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By

import os

USERNAME = os.environ.get("username")
PASSWORD = os.environ.get("password")


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_web_driver = Service(r"C:\Users\green\Downloads\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_web_driver)

driver.maximize_window()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3658277102&f_T=25169&geoId=100758706&keywords=python%20developer&location=Suffolk%2C%20England%2C%20United%20Kingdom&refresh=true&sortBy=R")
time.sleep(2)
login = driver.find_element(By.XPATH, value='/html/body/div[3]/header/nav/div/a[2]')
login.click()
username = driver.find_element(By.XPATH, value='//*[@id="username"]')
password = driver.find_element(By.XPATH, value='//*[@id="password"]')
username.send_keys(USERNAME)
password.send_keys(PASSWORD)
login_button = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
login_button.click()
time.sleep(1)
list_of_jobs = driver.find_element(By.CLASS_NAME, value="scaffold-layout__list-container")
jobs = list_of_jobs.find_elements(By.TAG_NAME, value="a")
for job in jobs:
    print(job)
    job.click()
    time.sleep(1)
    save_button = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
    save_button.click()
    time.sleep(3)