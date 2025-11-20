import random
from .models import Team, Player

def simulate_game(team1, team2, possessions=70):
    team1_score, team2_score = 0, 0
    team1_stats = {"fg_attempts": 0, "fg_made": 0, "3p_attempts": 0, "3p_made": 0, "ft_attempts": 0, "ft_made": 0, "turnovers": 0, "rebounds": 0}
    team2_stats = team1_stats.copy()  # simple for demo

    for i in range(possessions):
        # Randomly pick which team possesses the ball
        offense, defense, offense_stats = (team1, team2, team1_stats) if random.random() < 0.5 else (team2, team1, team2_stats)

        # Possession logic
        shot_type = random.choices(["2pt", "3pt", "turnover"], weights=[70, 20, 10])[0]
        if shot_type == "turnover":
            offense_stats['turnovers'] += 1
            continue
        
        shooter = random.choice(offense.players) if offense.players else None
        if not shooter:
            continue

        if shot_type == "2pt":
            offense_stats["fg_attempts"] += 1
            # FG% influenced by shooter rating (simplified)
            make = random.random() < (0.38 + 0.06 * (shooter.rating / 100))
            if make:
                offense_stats["fg_made"] += 1
                team1_score += 2 if offense is team1 else 0
                team2_score += 2 if offense is team2 else 0
                shooter.stats["points"] += 2
        elif shot_type == "3pt":
            offense_stats["3p_attempts"] += 1
            make = random.random() < (0.32 + 0.03 * (shooter.rating / 100))
            if make:
                offense_stats["3p_made"] += 1
                team1_score += 3 if offense is team1 else 0
                team2_score += 3 if offense is team2 else 0
                shooter.stats["points"] += 3

        # Free throws (after scoring, ~20% chance per made basket for demo)
        if make and random.random() < 0.2:
            offense_stats["ft_attempts"] += 2
            # Use rating for FT%
            ft_made = sum([1 if random.random() < (0.65 + 0.2 * (shooter.rating / 100)) else 0 for _ in range(2)])
            offense_stats["ft_made"] += ft_made
            team1_score += ft_made if offense is team1 else 0
            team2_score += ft_made if offense is team2 else 0
            shooter.stats["points"] += ft_made

    # Save team stats for future reference, then return scores
    team1.stats.update(team1_stats)
    team2.stats.update(team2_stats)
    return team1_score, team2_score
