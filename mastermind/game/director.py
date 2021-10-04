from code import Code
import random


class Director:
    """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
    """
    def __init__(self):
        self.code = Code()
        self.current = -1
        self.players = []
        self.name = []
        self.guess = []
        self.hint = []


    def add_player(self, players):
        for n in range(2):
            name = input(f"Enter a name for player {n + 1}: ")
            player = name                                 
            if player not in self.players:               
                self.players.append(players)

        self.current = (self.current + 1) % len(self.players)
        return self.players[self.current]

players = Director()
players.add_player(players)
print("-------------------------------\n")
print(f"Player {players.name} : ----, ****")
print(f"Player {players.name} : ----, ****")
print("-------------------------------\n")
print()
print("Guess the 4 digit number")
#player one
print(f"{players.current}'s turn:")
player_a = int(input("What is your guess? "))
print()
print("-------------------------------\n")
print(f"Player {players.name} : {players.guess}, {players.hint}")
print(f"Player {players.name} : ----, ****")
print("-------------------------------\n")
# player two
print(f"{players.current}'s turn:")
player_b = int(input("What is your guess? "))
print()
print("-------------------------------\n")
print(f"Player {players.name} : {players.guess}, {players.hint}")
print(f"Player {players.name} : {players.guess}, {players.hint}")
print("-------------------------------\n")

code = str(random.randint(1000, 10000))
if (player_a == code):
    print(f"{players} Won!")
elif (player_b == code):
    print(f"{players} Won!")
else:
    print("End of the Mastermind!")
