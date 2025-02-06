from get_dataset_with_selenium.get_team_urls import get_team_urls
from get_dataset_with_selenium.get_team_info import get_team_info
from get_dataset_with_selenium.get_team_technic_roster import get_team_technic_roster
from get_dataset_with_selenium.get_team_statistics import get_team_statistics
from get_dataset_with_selenium.get_team_matches import get_team_matches
from get_dataset_with_selenium.get_player_info import get_player_info
from get_dataset_with_selenium.save_to_excel import save_data_to_excel
from get_dataset_with_selenium.get_leaderboard_info import get_leaderboard_info

leagues = ["bsl"]  # List of leagues to collect data from
years = ["2024-2025", "2023-2024", "2022-2023", "2021-2022", "2020-2021", "2019-2020",
         "2018-2019", "2017-2018", "2016-2017", "2015-2016", "2014-2015", "2013-2014", "2012-2013",
         "2011-2012", "2010-2011"]

all_team_urls = []
processed_leagues = set()  # To ensure we fetch leaderboard only once per league-year

# Fetch leaderboard for each league-year combination (only once per league)
for league in leagues:
    for year in years:
        league_year = f"{league}-{year}"

        if league_year not in processed_leagues:
            print(f"\nFetching leaderboard for {league_year}...")
            leaderboard_data = get_leaderboard_info(league_year)

            if leaderboard_data:
                print("Leaderboard data retrieved successfully!")
                save_data_to_excel(leaderboard_data, "leaderboard.xlsx")
            else:
                print(f"Failed to retrieve leaderboard data for {league_year}.")

            processed_leagues.add(league_year)  # Mark as processed to avoid duplicate requests

        # Fetch team URLs for league-year
        team_urls = get_team_urls(league=league_year)
        all_team_urls.extend(team_urls)

print(f"Total {len(all_team_urls)} teams found.")

# Fetch data for each team
for team_url in all_team_urls:
    print(f"\nFetching data for {team_url}...")

    team_info = get_team_info(team_url)
    if team_info:
        print("Team info retrieved.")
        save_data_to_excel([team_info], "team_data.xlsx")  # Save immediately

        team_players = get_player_info(team_url, team_info["team_id"])
        if team_players:
            print("Player roster retrieved.")
            save_data_to_excel(team_players, "player_data.xlsx")

        technic_team_roster = get_team_technic_roster(team_url, team_info["team_id"])
        if technic_team_roster:
            print("Technical staff data retrieved.")
            save_data_to_excel(technic_team_roster, "technic_roster.xlsx")

        team_stats = get_team_statistics(team_url, team_info["team_id"])
        if team_stats:
            print("Player statistics retrieved.")
            save_data_to_excel(team_stats, "player_statistics.xlsx")

        team_matches = get_team_matches(team_url, team_info["team_id"])
        if team_matches:
            print("Match data retrieved.")
            save_data_to_excel(team_matches, "team_matches.xlsx")

print("\nAll data successfully retrieved and saved!")
