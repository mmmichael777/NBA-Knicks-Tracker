from nba_api.stats.static import teams

def get_team(team_abbreviation):
    return teams.find_team_by_abbreviation(team_abbreviation)


team = get_team("NYK")

print(team)

TEAM_NAME = "New York Knicks"
TEAM_ID = "1610612752"
CONFERENCE = "East"

TEAMS = {
  "Knicks": {
    "full name": "New York Knicks", 
    "id": 1610612752,
    "abbreviation": "NYK",
    "nickname": "Knicks",
    "Conference": "East",
  }, 

  "Celtics": {
    "name": "Boston Celtics", 
    "id": 
