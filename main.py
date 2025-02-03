from get_dataset_with_selenium.get_team_urls import get_team_urls
from get_dataset_with_selenium.get_team_info import get_team_info
from get_dataset_with_selenium.get_team_technic_roster import get_team_technic_roster
from get_dataset_with_selenium.get_team_statistics import get_team_statistics
from get_dataset_with_selenium.get_team_matches import get_team_matches
from get_dataset_with_selenium.get_player_info import get_player_info
from get_dataset_with_selenium.save_to_excel import save_data_to_excel  # Excel fonksiyonu

leagues = ["bsl"]  # Verileri toplanacak ligler
years = ["2024-2025","2023-2024","2022-2023","2021-2022","2020-2021","2019-2020",
         "2018-2019","2017-2018","2016-2017","2015-2016","2014-2015","2013-2014","2012-2013",
         "2011-2012","2010-2011"]
all_team_urls = []

# Takım URL'lerini al
for league in leagues:
    for year in years:
        league_year = league + "-" + year
        team_urls = get_team_urls(league=league_year)
        all_team_urls.extend(team_urls)

print(f"Toplam {len(all_team_urls)} takım bulundu.")

# Her takım için verileri çek
for team_url in all_team_urls:
    print(f"\n{team_url} için veri çekiliyor...")

    team_info = get_team_info(team_url)
    if team_info:
        print("Takım bilgileri alındı.")
        save_data_to_excel([team_info], "team_data.xlsx")  # Hemen kaydet

        team_players = get_player_info(team_url, team_info["team_id"])
        if team_players:
            print("Kadro bilgileri alındı.")
            save_data_to_excel(team_players, "player_data.xlsx")  # Hemen kaydet

        technic_team_roster = get_team_technic_roster(team_url, team_info["team_id"])
        if technic_team_roster:
            print("Teknik kadro bilgileri alındı.")
            save_data_to_excel(technic_team_roster, "technic_roster.xlsx")  # Hemen kaydet

        team_stats = get_team_statistics(team_url, team_info["team_id"])
        if team_stats:
            print("Oyuncu istatistikleri alındı.")
            save_data_to_excel(team_stats, "player_statistics.xlsx")  # Hemen kaydet

        team_matches = get_team_matches(team_url, team_info["team_id"])
        if team_matches:
            print("Takım maçları alındı.")
            save_data_to_excel(team_matches, "team_matches.xlsx")  # Hemen kaydet

print("\nTüm veriler başarıyla çekildi ve kaydedildi.")
