
# Premier League match analysis

# You're a Data Analyst at a sports analytical company(like opta sports, sofascore)
# Your job is to analyse match statistics to provide insights for punters, team managers,
# sports journalistsand fantasy football players.
# You're required to analyse goal-scoring patterns from the latest gameweek

# Sports analytics companies use exact techniques to power platforms like FPL, betting odds, tactical analysis

# The Problem
# We have goal data from 10 PL matches in a game week, and are required to:
# 1. Count how many goals each team scored.
# 2. Find the highest scoring teams and matches
# 3. Calculate goal statistics (average goals per match, most prolific teams)
# 4. Identify teams in good forms vs struggling teams.
# 5. Generate insight for pundits and fantasy team managers

from pprint import pprint

gameweek_matches = [
    {"match_id": 1, "home_team": "Arsenal", "away_team": "Brighton", 
     "home_goals": 3, "away_goals": 0, "venue": "Emirates Stadium"},

    {"match_id": 2, "home_team": "Liverpool", "away_team": "Bournemouth", 
     "home_goals": 4, "away_goals": 1, "venue": "Anfield"},

    {"match_id": 3, "home_team": "Man City", "away_team": "Everton", 
     "home_goals": 2, "away_goals": 1, "venue": "Etihad Stadium"},

    {"match_id": 4, "home_team": "Chelsea", "away_team": "Wolves", 
     "home_goals": 3, "away_goals": 1, "venue": "Stamford Bridge"},

    {"match_id": 5, "home_team": "Newcastle", "away_team": "Fulham", 
     "home_goals": 2, "away_goals": 2, "venue": "St James' Park"},

    {"match_id": 6, "home_team": "Aston Villa", "away_team": "Man United", 
     "home_goals": 1, "away_goals": 2, "venue": "Villa Park"},

    {"match_id": 7, "home_team": "Tottenham", "away_team": "Brentford", 
     "home_goals": 2, "away_goals": 2, "venue": "Tottenham Hotspur Stadium"},

    {"match_id": 8, "home_team": "West Ham", "away_team": "Crystal Palace", 
     "home_goals": 0, "away_goals": 1, "venue": "London Stadium"},

    {"match_id": 9, "home_team": "Nottingham Forest", "away_team": "Sheffield United", 
     "home_goals": 1, "away_goals": 0, "venue": "City Ground"},

    {"match_id": 10, "home_team": "Luton Town", "away_team": "Burnley", 
     "home_goals": 1, "away_goals": 1, "venue": "Kenilworth Road"}
]

print("\n PREMIER LEAGUE GAMEWEEK 18 ANALYSIS")
print("="*60)

# STEP 1 Extract goals per team
# Concept - process a list of dictionaries to aggregate team statistics


team_goals = {}

for match in gameweek_matches:
   # extra match data
   home_team = match["home_team"]
   away_team = match["away_team"]
   home_goals = match["home_goals"]
   away_goals = match["away_goals"]

   # get goals for home team
   team_goals[home_team] = home_goals

   # get golas for away team
   team_goals[away_team] = away_goals

pprint(team_goals)
print("")

print("\nGOALS SCORED BY TEAM")
for(team, goals) in team_goals.items():
   print(f"  {team}: {goals} goal(s)")

# Step 2 Highest scoring teams and matches

goals_threshold = 3

highest_scoring_teams = {}
highest_scoring_matches = []


for(teams, goals) in team_goals.items():
   if goals >= goals_threshold:
      highest_scoring_teams[teams] = goals

      for game in gameweek_matches:
         if game["home_team"] == teams or game["away_team"]  == teams:
            temp_games = game.copy()
            del temp_games["venue"]

            if temp_games not in highest_scoring_matches:
               highest_scoring_matches.append(temp_games)

pprint(gameweek_matches)

print("\nHighest Scoring teams")
pprint(highest_scoring_teams)



print("\nHighest Scoring matches")
pprint(highest_scoring_matches)

    

   
   









