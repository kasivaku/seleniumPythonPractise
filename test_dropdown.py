import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(3)

driver.get("https://letcode.in/dropdowns")

select_fruit = driver.find_element(By.ID, "fruits")
selectFruit = Select(select_fruit)
# First example
selectFruit.select_by_visible_text("Banana")
notif = driver.find_element(By.CLASS_NAME, "subtitle")
print(notif.text)
assert ("Banana" in notif.text)
time.sleep(3)
# Second example
select_country = driver.find_element(By.ID, "country")
selectCountry = Select(select_country)
selectCountry.select_by_value("Peru")
print(selectCountry.first_selected_option.text)
assert selectCountry.first_selected_option.text == "Peru"
driver.close()

# Third Example

select_hero = driver.find_element(By.ID, "superheros")
selectHero = Select(select_hero)

print("Checking if its a multi select -" + str(selectHero.is_multiple))
print("All available option- ")
for item in selectHero.options:
    print(item.text)
selectHero.select_by_value("am")
selectHero.select_by_index(2)
selectHero.select_by_visible_text("Daredevil")
print("After selecting - ")
for sel in selectHero.all_selected_options:
    print(sel.text)
time.sleep(3)

selectHero.deselect_all()
print("After deselecting - " + str(selectHero.all_selected_options))
time.sleep(2)
