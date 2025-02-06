from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def get_leaderboard_info(league):
    """Fetches the leaderboard (standings) for the given league and season."""

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(f"https://www.tbf.org.tr/ligler/{league}/puan-durumu")
    time.sleep(2)

    leaderboard_data = []

    try:
        leaderboard_teams = driver.find_elements(By.XPATH, '//*[@id="TableMaclar"]/tbody/tr[@class="popper-links"]')

        for team in leaderboard_teams:
            team_data = {
                "league": league
            }
            team_data["team_rank"] = team.find_element(By.XPATH, ".//td[@class='align-middle text-center relagation sorting_1']/span").text
            team_data["team_name"] = team.find_element(By.XPATH, ".//td[@class='text-left']").text
            team_data["team_matches_played"] = team.find_element(By.XPATH, ".//td[5]").text
            team_data["team_wins"] = team.find_element(By.XPATH, ".//td[6]").text
            team_data["team_losses"] = team.find_element(By.XPATH, ".//td[7]").text
            team_data["team_points_scored"] = team.find_element(By.XPATH, ".//td[8]").text
            team_data["team_points_conceded"] = team.find_element(By.XPATH, ".//td[9]").text
            team_data["team_home_points"] = team.find_element(By.XPATH, ".//td[10]").text
            team_data["team_home_goal_difference"] = team.find_element(By.XPATH, ".//td[11]").text
            team_data["team_total_goal_difference"] = team.find_element(By.XPATH, ".//td[12]").text
            team_data["team_total_points"] = team.find_element(By.XPATH, ".//td[13]").text

            leaderboard_data.append(team_data)

        driver.quit()
        return leaderboard_data

    except Exception as e:
        print(f"Error fetching leaderboard for {league}: {e}")
        driver.quit()
        return []
