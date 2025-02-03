from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def get_team_technic_roster(team_url, team_id):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(team_url + "/teknik-kadro")
    time.sleep(2)

    league = team_url.split("/")[-3]
    team_technic_roster_data = []  # Liste olarak değiştirildi

    try:
        technic_roster = driver.find_elements(by=By.XPATH, value='/html/body/form/div[6]/div/div[2]/div/div/div[@class="col-md-2 col-4 text-center mt-4"]')

        for technic_member in technic_roster:
            technic_roster_data = {
                "team_id": team_id,
                "team_url": team_url,
                "league": league
            }
            technic_member_name = technic_member.find_element(by=By.XPATH, value=".//h5").get_attribute("textContent")
            technic_roster_data["technic_member_name"] = technic_member_name

            technic_member_role = technic_member.find_element(by=By.XPATH, value=".//p").get_attribute("textContent")
            technic_roster_data["technic_member_role"] = technic_member_role

            team_technic_roster_data.append(technic_roster_data)  # Listeye ekleme yapıldı

        driver.quit()
        return team_technic_roster_data  # Liste olarak döndürülüyor

    except Exception as e:
        print(f"Hata oluştu: {e}")
        driver.quit()
        return []
