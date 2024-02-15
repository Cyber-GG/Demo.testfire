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

totp = pyotp.TOTP('XXUUNAVCYKI3UGHPCWUMVCUHZSYOLMTL')
print(totp.now())

element=driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]/div[3]/form/div[1]/div/input[1]")

# Check if the element is visible
if element.is_displayed():
    print("Login Page visible")
    usernameid=driver.find_element(By.ID, "username")
    passwordid=driver.find_element(By.ID, "password")
    usernameid.send_keys(username)
    passwordid.send_keys(password)
    loginbutton = driver.find_element(By.ID, "Login")
    loginbutton.click()
    time.sleep(10)
    verify = driver.page_source
    print("Sarada")
    #print(verify)
    current_url = driver.current_url
    print(current_url)
    env_file = os.environ(current_url)
    with open(env_file, "a") as myfile:
       myfile.write("MY_VAR=MY_VALUE")
    print(MY_VAR)
 
else:
    print("Login page not loaded")

