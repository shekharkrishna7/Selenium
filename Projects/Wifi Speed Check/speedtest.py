from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

path = "../../chromedriver.exe"

driver = webdriver.Chrome(path)

print("STARTING TEST...")

driver.get("https://www.speedtest.net/")

driver.implicitly_wait(5)

print("WEBSITE LOADED...")

driver.find_element(By.LINK_TEXT, "GO").click()

time.sleep(40)

ping = driver.find_element(By.CSS_SELECTOR, "span[class='result-data-large number result-data-value "
                                            "ping-speed']").text

download_speed = driver.find_element(By.CSS_SELECTOR, "span[class='result-data-large number result-data-value "
                                                      "download-speed']").text

upload_speed = driver.find_element(By.CSS_SELECTOR, "span[class='result-data-large number result-data-value "
                                                    "upload-speed']").text

print(f"PING: {ping}ms")
print(f"DOWNLOAD SPEED: {download_speed}Mbps")
print(f"UPLOAD SPEED: {upload_speed}Mbps")

print("----------------")
print("TEST ENDED")
print("----------------")

driver.quit()
