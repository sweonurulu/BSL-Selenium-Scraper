from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def get_team_matches(team_url, team_id):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(team_url + "/maclar")
    time.sleep(2)

    team_match_data = []  # Liste olarak tanımlandı

    try:
        team_matches = driver.find_elements(By.XPATH, '//*[@id="TableDocuments"]/tbody/tr')

        for match in team_matches:
            match_data = {}

            try:
                match_data["league"] = team_url.split("/")[-3]
                match_data["team_id"] = team_id
                match_data["team_url"] = team_url

                match_data["match_id"] = match.find_element(By.XPATH, './/td[1]').get_attribute("data-link").split("/")[-1]
                match_data["is_played"] = match.find_element(By.XPATH, './/td[1]').get_attribute("data-durum")
                match_data["match_date"] = match.find_element(By.XPATH, './/td[1]').text

                match_data["match_hour"] = match.find_element(By.XPATH, './/td[2]').text
                match_data["match_week"] = match.find_element(By.XPATH, './/td[3]').text
                match_data["enemy_team"] = match.find_element(By.XPATH, './/td[4]').text
                match_data["match_score_result"] = match.find_element(By.XPATH, './/td[5]').text
                match_data["match_city"] = match.find_element(By.XPATH, './/td[8]').text
                match_data["match_saloon"] = match.find_element(By.XPATH, './/td[9]').text

                # match_result: i etiketinin class bilgisine göre "W" veya "L" belirleme
                try:
                    i_element_result = match.find_element(By.XPATH, './/td[6]/i')
                    i_class_result = i_element_result.get_attribute("class")

                    match_data["match_result"] = "W" if "text-c-league" in i_class_result else "L"
                except:
                    match_data["match_result"] = "Unknown"

                # match_field: i etiketinin class bilgisine göre "HOME" veya "GUEST" belirleme
                try:
                    i_element_field = match.find_element(By.XPATH, './/td[7]/i')
                    i_class_field = i_element_field.get_attribute("class")

                    if "fa-home" in i_class_field:
                        match_data["match_field"] = "HOME"
                    elif "fa-plane" in i_class_field:
                        match_data["match_field"] = "GUEST"
                    else:
                        match_data["match_field"] = "Unknown"
                except:
                    match_data["match_field"] = "Unknown"

                team_match_data.append(match_data)  # Dict verisini doğrudan listeye ekledik

            except Exception as e:
                print(f"Bir maçın verileri çekilirken hata oluştu: {e}")

        driver.quit()
        return team_match_data  # Liste olarak döndürülüyor

    except Exception as e:
        print(f"Hata oluştu: {e}")
        driver.quit()
        return None