import random
from .models import Team, Player

def simulate_game(team1, team2):
    # Very simple simulation—refine for realistic results
    score1, score2 = 0, 0
    for p in team1.players:
        p_points = int(random.gauss(p.rating, 5))
        score1 += p_points
        p.stats["points"] += p_points
        p.stats["fg_attempts"] += random.randint(10, 20)
        p.stats["fg_made"] += int(p.stats["fg_attempts"] * (0.4 + 0.1 * (p.rating/100)))
    for p in team2.players:
        p_points = int(random.gauss(p.rating, 5))
        score2 += p_points
        p.stats["points"] += p_points
        p.stats["fg_attempts"] += random.randint(10, 20)
        p.stats["fg_made"] += int(p.stats["fg_attempts"] * (0.4 + 0.1 * (p.rating/100)))
    team1.stats["games_played"] += 1
    team2.stats["games_played"] += 1
    if score1 > score2:
        team1.stats["wins"] += 1
        team2.stats["losses"] += 1
    else:
        team2.stats["wins"] += 1
        team1.stats["losses"] += 1
    return score1, score2