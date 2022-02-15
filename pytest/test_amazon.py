from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest

#launching the website via chromedriver

@pytest.fixture()
def test_setup():
    global driver
    s = Service("/Users/mertkav/Downloads/chromedriver")
    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("test completed")

#identifying and searching "Shoes" using locator (x_path)

def test_searchbar(test_setup):
    global driver
    driver.get("https://www.amazon.com/")
    Search_Bar = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']" )
    Search_Bar.send_keys("Shoes")
    Click_Search_Button = driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']" )
    Click_Search_Button.click()
    driver.implicitly_wait(8)

#Selecting the second shoes

    Second_Shoes = driver.find_element(By.XPATH, "//body/div[@id='a-page']/div[@id='search']/div[1]/div[1]/div[1]/span[3]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/h2[1]")
    Second_Shoes.click()




