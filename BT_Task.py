import os
from dotenv import load_dotenv
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# read url from the env file
MY_ENV_VAR = os.getenv('URL')

# drive initialization
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open the URL
driver.get(MY_ENV_VAR)

try:
    # Close the cookie pop-up if it appears
    cookie_popup = driver.find_element(By.CLASS_NAME, "mainContent")
    if cookie_popup.is_displayed():
        cookie_popup.find_element(By.CLASS_NAME, "call").click()

    # Hover to Mobile menu
    mobile_menu = driver.find_element(By.XPATH, '//*[@id="bt-navbar"]/div[2]/div[2]/div/div[1]/div[1]/ul/li[4]')

    ActionChains(driver).move_to_element(mobile_menu).perform()

    # Wait for the Mobile phones submenu to appear (you may need to adjust the timeout)
    mobile_submenu = driver.find_element(By.XPATH, '//*[@id="bt-navbar"]/div[2]/div[2]/div/div[1]/div[1]/ul/li[4]/a')
    WebDriverWait(driver, 10).until(EC.visibility_of(mobile_submenu))

    # Click on Mobile phones
    mobile_menu.click()

    # Verify the number of banners present below “See Handset details”
    banners = driver.find_elements(By.XPATH, "//div[@class='offers-slider__slide']")
    assert len(banners) >= 3, "Number of banners is less than 3"

    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Click View SIM only deals
    sim_deals_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div/div[2]/div/a[2]')
    sim_deals_button.click()

    # Validate the title for the new page
    expected_title = "SIM Only Deals | Compare SIMO Plans & Contracts | BT Mobile"
    assert driver.title == expected_title, f"Page title is not as expected. Got: {driver.title}"

finally:
    # Close the browser
    driver.quit()
