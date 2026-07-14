import statsapi as mlb
from lib.season import Season_Stats

if __name__ == "__main__":
    date = input("Year: ").strip()
    season_stats = Season_Stats(year=date)
    print("Runs per game:", season_stats.rpg)