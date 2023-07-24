import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_web_driver = Service(r"C:\Users\green\Downloads\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_web_driver)

driver.maximize_window()
driver.get("http://orteil.dashnet.org/experiments/cookie/")