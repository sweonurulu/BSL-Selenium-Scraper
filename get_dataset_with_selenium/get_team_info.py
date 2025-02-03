from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def get_team_info(team_url):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(team_url)
    team_id = team_url.split("/")[-1]
    time.sleep(5)

    team_data = {"team_id": team_id, "team_url": team_url}

    try:
        team_name = driver.find_element(By.XPATH, "//h1[@class='text-c-league custom-font-bold mt-1 mb-1']").get_attribute("textContent")
        team_data["team_name"] = team_name
        team_data["league"] = team_data["team_url"].split("/")[-3]

        team_city_year = driver.find_element(By.XPATH, "//div[@class='row text-center justify-content-center']//h4").get_attribute("textContent")
        team_city = team_city_year.split("|")[0].split(": ")[-1].strip()
        team_year = team_city_year.split("|")[-1].split(": ")[-1].strip()
        team_data["team_city"] = team_city
        team_data["team_year"] = team_year

        team_saloon_infos = driver.find_elements(By.XPATH, "//div[@id='body_pnl']//div[@class='row text-center justify-content-center']//span[@class='cursor-help']")

        if len(team_saloon_infos) >= 3:
            team_data["saloon_name"] = team_saloon_infos[0].get_attribute("textContent")
            team_data["saloon_capacity"] = team_saloon_infos[1].get_attribute("textContent")
            team_data["saloon_address"] = team_saloon_infos[2].get_attribute("textContent")

        driver.quit()
        return team_data

    except Exception as e:
        print(f"Hata oluştu: {e}")
        driver.quit()
        return None
