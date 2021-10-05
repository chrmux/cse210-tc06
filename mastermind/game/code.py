class Code:
    """A designated playing surface. The responsibility of Board is to keep track of the pieces in play.
    
    Stereotype: 
        Information Holder
    Attributes:
        value (list): Returns the value of the code as a string.
    """

    def __init__(self):
        """The class constructor.
        """
        self.value = []


    
    def generate_code(self, code, guess):
        """Generates a hint based on the given code and guess.

    Args:
        self (Board): An instance of Board.
        code (string): The code to compare with.
        guess (string): The guess that was made.

    Returns:
        string: A hint in the form [xxxx]
    """
        hint = ''      
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += "x"
            elif letter in guess:
                hint += "o"
            else:
                hint += "*"
        return hint
  
