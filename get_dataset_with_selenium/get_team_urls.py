from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


def get_team_urls(league):
    url_takimlar = "https://www.tbf.org.tr/ligler/" + league + "/takimlar"

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(url_takimlar)
    time.sleep(2)

    team_elements = driver.find_elements(By.XPATH, "//div[@class='col-6 col-md-3 d-flex align-items-stretch']//a")
    team_urls = [team.get_attribute("href") for team in team_elements]

    driver.quit()

    return team_urls
