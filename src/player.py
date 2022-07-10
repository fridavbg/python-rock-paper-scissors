
class Player:
    """
    Class representing a Player
    """
    def __init__(self, player_type, name):
        self.totalWins = 0
        self.name = name
        self.player_type = player_type
        self.currentHand = ''
        # location 

    def get_player_info(self):
        return f"Player name: {self.name}\nPlayer type: {self.player_type}\nTotalwins: {self.totalWins}\nCurrentHand:{self.currentHand}"
