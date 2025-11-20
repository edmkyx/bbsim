class Player:
    def __init__(self, name, rating, position):
        self.name = name
        self.rating = rating
        self.position = position
        self.stats = {
            "points": 0,
            "rebounds": 0,
            "assists": 0,
            "fg_attempts": 0,
            "fg_made": 0,
        }

class Team:
    def __init__(self, name, players=None):
        self.name = name
        self.players = players if players is not None else []
        self.stats = {
            "wins": 0,
            "losses": 0,
            "games_played": 0,
        }