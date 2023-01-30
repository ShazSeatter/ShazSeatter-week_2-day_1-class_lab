class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player_name):
        return player_name in self.players

        # for player in self.players:
        #     if player == player_name:
        #         return True
        # return False

#  SOMETHING TO REMEMBER
        # return self.players.count(player) > 0

    def play_game(self, has_won):
        if has_won:
            self.points += 3

            
