from models.players import Player

class Game():

    def __init__(self, player_1, player_2):
       self.player_1 = player_1
       self.player_2 = player_2


    def play_new_game(self, game):

        if game.player_1.move == "rock" and game.player_2.move == "scissors":
            return player_1
        if game.player_1.move == "rock" and game.player_2.move == "paper":
            return player_2
        if game.player_1.move == "paper" and game.player_2.move == "rock":
            return player_1
        if game.player_1.move == "paper" and game.player_2.move == "scissors":
            return player_2
        if game.player_1.move == "scissors" and game.player_2.move == "paper":
            return player_1
        if game.player_1.move == "scissors" and game.player_2.move == "rock":
            return player_2
        if game.player_1.move == game.player_2.move:
            return None

    # def pc_choice(self):
    #     moves_list = ["rock", "paper", "scissors"]
    #     pc_move = random.choice(moves_list)
    #     return pc_move