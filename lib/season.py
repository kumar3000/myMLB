import statsapi as mlb

class Season_Stats:
    year: int
    stats: dict
    rpg: float
    
    def __init__(self, year: int):
        self.year = year
        self.stats = mlb.game_pace_data(season=year)
        self.rpg = self.stats.get("sports")[0].get("runsPerGame")
    
    def get_rpg(self) -> float:
        return self.rpg