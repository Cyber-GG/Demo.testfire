from selenium import webdriver
import pyotp
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import os


firefox_options = Options()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--disable-gpu')
firefox_options.add_argument("--no-sandbox");
firefox_options.add_argument("--disable-dev-shm-usage");

username = "gomathy.gopinath@qualitestgroup.com.perftestin"
password = "Password@3101"

driver = webdriver.Firefox(options = firefox_options)
driver.get('https://saint-gobain-uk--perftestin.sandbox.my.salesforce.com/')
current_url = driver.current_url
print(current_url)
#totp = pyotp.TOTP('XXUUNAVCYKI3UGHPCWUMVCUHZSYOLMTL')
#totp.now()

#element=driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]/div[3]/form/div[1]/div/input[1]")

# Check if the element is visible
#if element.is_displayed():
usernameid=driver.find_element(By.ID, "un")
passwordid=driver.find_element(By.ID, "pw")
usernameid.send_keys(un)
passwordid.send_keys(pw)
loginbutton = driver.find_element(By.ID, "Login")
loginbutton.click()
current_url = driver.current_url
print(current_url)
time.sleep(10)
current_url = driver.current_url
print(current_url)
verify = driver.page_source
#print(verify)
current_url = driver.current_url
print(current_url)
