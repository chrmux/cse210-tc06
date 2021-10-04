from code import Code
import random


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        code (Hunter): An instance of the class of objects known as Code.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.code = Code()
        self.current = -1
        self.players = []
        self.name = []
        self.guess = []
        self.hint = []


    def get_code(self, player_name):
        for n in range(2):
            name = input(f"Enter a name for player {n + 1}: ")
            player = name                                 
            if player not in self.players:               
                self.players.append(player_name)

            player_name = (self.current + 1) % len(self.players)
        return player_name

players = Director()
players.get_code(players)
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
