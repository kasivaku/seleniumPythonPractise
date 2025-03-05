import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://letcode.in/") # Launch the url in chrome
driver.maximize_window()    # Maximize the window
print(driver.current_url)   # Show current url
print(driver.title)     # Show page title
driver.find_element(By.XPATH, "//a[text()='Log in']").click()
driver.find_element(By.NAME,"email").send_keys("koushik350@gmail.com")
driver.find_element(By.NAME,"password").send_keys("Pass123$")
driver.find_element(By.XPATH,"//button[text()='LOGIN']").click()


prop_value = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@role='alertdialog']"))).get_dom_attribute("aria-label")
print("Value from toast message = ",prop_value)
assert prop_value=="Welcome Koushik Chatterjee"
time.sleep(7)
driver.find_element(By.LINK_TEXT,"Sign out").click()
time.sleep(5)    # for 3 seconds delay to see the execution
driver.close()  # Close the current browser window