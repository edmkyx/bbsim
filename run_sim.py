from app.models import Player, Team
from app.sim import simulate_game

# Sample teams
team1 = Team(
    name="College A",
    players=[
        Player("PG1", 80, "PG"),
        Player("SG1", 75, "SG"),
        Player("SF1", 70, "SF"),
        Player("PF1", 68, "PF"),
        Player("C1", 74, "C"),
    ],
)
team2 = Team(
    name="College B",
    players=[
        Player("PG2", 78, "PG"),
        Player("SG2", 72, "SG"),
        Player("SF2", 71, "SF"),
        Player("PF2", 70, "PF"),
        Player("C2", 77, "C"),
    ],
)

score1, score2 = simulate_game(team1, team2)

print(f"{team1.name} {score1} - {team2.name} {score2}")
for player in team1.players + team2.players:
    print(f"{player.name} ({player.position}) - {player.stats['points']} pts")
