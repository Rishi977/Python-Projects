

from os import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

 # type: ignore

# Set path to your ChromeDriver
driver_path = "/opt/homebrew/bin/chromedriver"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 10)


#Open the demo website
driver.get("https://sit.gts.nec.com:4443/")
driver.maximize_window()

#Login the page
#open the dropdown
driver.find_element(By.ID,"select2-CompanyCodeSel-container").click()

#type into the dropdown search input
dropdown_search = driver.find_element(By.CLASS_NAME, "select2-selection__arrow")
dropdown_search = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "select2-search__field")))

time.sleep(1)

#press enter after selection of dropdown
dropdown_search.send_keys("APAC L2")
dropdown_search.send_keys(Keys.RETURN)

driver.find_element(By.ID,"EmailId").send_keys("pradumna.shrivastava@india.nec.com")
driver.find_element(By.ID,"loginPassword").send_keys("abc@12345")

#scroll and click login
driver.find_element(By.ID, "btnLogin").click()

input("Enter any thing to close browser")

time.sleep(50)
#driver.quit()
