import statsapi as mlb

class Season_Stats:
    year: int
    stats: dict
    rpg: float
    
    def __init__(self, year: int):
        stats = mlb.game_pace_data(season=year)
        self.rpg = stats.get("sports")[0].get("runsPerGame")