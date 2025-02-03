from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def get_player_info(team_url, team_id):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(team_url + "/basketbolcular")
    time.sleep(2)

    roster_data = []  # Liste olarak değiştirildi

    try:
        roster = driver.find_elements(by=By.XPATH, value='/html/body/form/div[6]/div/div[2]/div/div[@class="row mt-4"]')
        league = team_url.split("/")[-3]

        for player in roster:
            player_data = {
                "team_id": team_id,
                "team_url": team_url,
                "league": league
            }
            player_data["player_name"] = player.get_attribute("data-filter")

            player_data["player_id"] = player.find_element(By.XPATH,
                                                             value=".//div[@class='col-lg-10 col-md-12 text-center text-lg-left']"
                                                                   "/h2/a").get_attribute("href").split("/")[-1]
            player_birthdate_height = player.find_element(By.XPATH,
                                                             value=".//div[@class='col-lg-10 col-md-12 text-center text-lg-left']"
                                                                   "/h5").text.split("|")

            player_data["player_birthdate"] = player_birthdate_height[0]

            if player_birthdate_height[1]!="":
                player_data["player_height"] = player_birthdate_height[-1]

            else:
                player_data["player_height"] = "unknown"

            roster_data.append(player_data)

        driver.quit()
        return roster_data

    except Exception as e:
        print(f"Hata oluştu: {e}")
        driver.quit()
        return []
