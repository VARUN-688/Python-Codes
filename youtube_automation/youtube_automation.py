from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def automation(search:str):
    driver = webdriver.Chrome("chromedriver.exe")
    time.sleep(1)
    driver.get("https://www.youtube.com")
    time.sleep(1)
    driver.maximize_window()
    time.sleep(1)
    driver.find_element(By.NAME, "search_query").send_keys(search)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "style-scope ytd-searchbox").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "style-scope ytd-video-renderer").click()
    time.sleep(1000)
if __name__=="__main__":
    automation(input('enter the search-> '))
