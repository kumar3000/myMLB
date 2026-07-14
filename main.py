import statsapi as mlb

def get_standings(leagueId: str, date: str):
    return mlb.standings(leagueId=leagueId,date=date)

if __name__ == "__main__":
    date = input()
    leagueId = input()
    print( get_standings(leagueId, date) )