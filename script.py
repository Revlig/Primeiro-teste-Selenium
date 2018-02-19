from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox(executable_path="/home/gilver_souza/drivers/geckodriver")
driver.get("https://github.com/")
assert "GitHub" in driver.title
elem = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div/span/div/a[1]")
elem.click()

names = ["carlos", "margot", "paulo"]
passwd = ["gitsenha", "testsenha", "passwd"]
for inputs in range(0, len(names)):

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "login_field"))
            )
    finally:
        username = driver.find_element_by_id("login_field")


    username.clear()
    username.send_keys(names[inputs])

    password = driver.find_element_by_id("password")
    password.clear()
    password.send_keys(passwd[inputs])

    button_sign_in = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/form/div[4]/input[3]")
    button_sign_in.click()