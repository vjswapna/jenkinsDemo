from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
driver.implicitly_wait(10)
driver.find_element(By.NAME,"Email").clear()
driver.find_element(By.NAME,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.NAME,"Password").clear()
driver.find_element(By.NAME,"Password").send_keys("admin")
time.sleep(10)

driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
time.sleep(10)

actual_title=driver.title
expected_tile="Dasboard/noncommerce adminstration"

if actual_title==expected_tile:
    print("Title verification passed")
else:
    print("Title verification failed")
driver.close()
driver.quit()
