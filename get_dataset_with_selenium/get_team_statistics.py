from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


def get_team_statistics(team_url, team_id):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(team_url + "/istatistik")
    time.sleep(2)

    team_stat_data = []  # Liste olarak değiştirildi


    try:
        player_statistics = driver.find_elements(By.XPATH, '//*[@id="FilterPlayer"]/tbody/tr')

        league = team_url.split("/")[-3]

        for player_stat in player_statistics:
            player_data = {}

            try:
                player_data["league"] = league
                player_data["team_id"] = team_id
                player_data["team_url"] = team_url

                player_data["player_no"] = player_stat.find_element(By.XPATH, './/td[1]').text
                if player_data["player_no"] == "":
                    break

                player_data["player_name"] = player_stat.find_element(By.XPATH, './/td[3]').text
                player_data["player_id"] = player_stat.find_element(By.XPATH, './/td[3]//a').get_attribute("href").split("/")[-1]

                player_data["player_match_no"] = player_stat.find_element(By.XPATH, './/td[@class="text-center font-weight-bold text-c-league"]').text
                player_data["player_played_time"] = player_stat.find_element(By.XPATH, './/td[5]').text
                player_data["player_points"] = player_stat.find_element(By.XPATH, './/td[6]').text
                player_data["player_tried_shoots_number"] = player_stat.find_element(By.XPATH, './/td[7]').text
                player_data["player_2x_points_number"] = player_stat.find_element(By.XPATH, './/td[8]').text
                player_data["player_3x_points_number"] = player_stat.find_element(By.XPATH, './/td[9]').text
                player_data["player_free_throw_number"] = player_stat.find_element(By.XPATH, './/td[10]').text
                player_data["player_defense_rebounds_number"] = player_stat.find_element(By.XPATH, './/td[11]').text
                player_data["player_offense_rebounds_number"] = player_stat.find_element(By.XPATH, './/td[12]').text
                player_data["player_total_rebounds_number"] = player_stat.find_element(By.XPATH, './/td[13]').text
                player_data["player_assists_number"] = player_stat.find_element(By.XPATH, './/td[14]').text
                player_data["player_blocks_number"] = player_stat.find_element(By.XPATH, './/td[15]').text
                player_data["player_stealing_ball_number"] = player_stat.find_element(By.XPATH, './/td[16]').text
                player_data["player_loss_ball_number"] = player_stat.find_element(By.XPATH, './/td[17]').text
                player_data["player_foul_number"] = player_stat.find_element(By.XPATH, './/td[18]').text
                player_data["player_contribute_game_number"] = player_stat.find_element(By.XPATH, './/td[19]').text
                player_data["player_efficiency_score"] = player_stat.find_element(By.XPATH, './/td[20]').text

                team_stat_data.append(player_data)  # Doğrudan listeye ekleme yapıldı

            except Exception as e:
                print(f"Bir oyuncunun verileri çekilirken hata oluştu: {e}")

        driver.quit()
        return team_stat_data  # Liste olarak döndürülüyor

    except Exception as e:
        print(f"Hata oluştu: {e}")
        driver.quit()
        return None
