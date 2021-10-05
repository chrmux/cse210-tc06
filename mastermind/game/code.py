class Code:
    """A designated playing surface. The responsibility of Board is to keep track of the pieces in play.
    
    Stereotype: 
        Information Holder
    Attributes:
        code (Code): An instance of the class of objects known as Code.
        
    """

    def __init__(self):
        """
        value (list): Returns the value of the code as a string.
        """
        self.value = []


    
    def generate_code(self, players):
        """
        Print the user input
        """
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
  
