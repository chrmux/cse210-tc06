from code import Code
import random


class Director:
    """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        
        self.current = -1
        self.players = []
        self._code = Code()


    def get_code(self, player_name):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
        """
        player1 = str(input("Enter a name for player 1: "))
        player2 = str(input("Enter a name for player 2: "))
        guess = "----"
        hint = "****"
        hint = self._code.generate_code(guess, hint)
        # print out the player names
        print("-------------------------------\n")
        print(f"Player {player1} : ----, ****")
        print(f"Player {player2} : ----, ****")
        print("-------------------------------\n")
        #player one
        print(f"{player1}'s turn:")
        player_1 = int(input("What is your guess? "))
        print()
        print("-------------------------------\n")
        print(f"Player {player1} : {player_1}, {hint}")
        print(f"Player {player2} : {guess}, {hint}")
        print("-------------------------------\n")
        # player two
        print(f"{player2}'s turn:")
        player_2 = int(input("What is your guess? "))
        print()
        print("-------------------------------\n")
        print(f"Player {player1} : {player_1}, {hint}")
        print(f"Player {player2} : {player_2}, {hint}")
        print("-------------------------------\n")
        
        
        code = str(random.randint(1000, 10000))
        player_name = code
        if player_1 == code:
            print(f"{player_1} Won!")
        elif player_2 == code:
            print(f"{player_2} Won!")
        else:

            print("\n\nGreat, you got it in", player_name,  "guesses!")
            

    def start_game(self):
        "Start the game loop"       
        players = Director()
        players.get_code(players)
