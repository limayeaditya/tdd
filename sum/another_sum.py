import re

class NegativeNumberError(ValueError):
    """Custom exception for handling negative number scenarios."""
    def __init__(self, negative_array) -> None:
        self.negative_array = negative_array
        super().__init__(f"negative numbers not allowed {self.negative_array}")

class SeparatorsAtEndError(ValueError):
    """Custom exception for handling separators at end scenarios."""
    def __init__(self) -> None:
        super().__init__(f"separators not allowed at the end")


class Parser:
    """Class responsible for parsing and validating numbers from an input string."""

    def __init__(self, number_string="") -> None:
        self.number_string = number_string
        self.separator = ""

    def split_string(self):
        # Split the input string using commas, semicolons, or newlines as delimiters
        if self.number_string and self.number_string[-1].isdigit():
            if self.number_string[0:2] == "//":
                self.separator = self.change_delimiter()
            number_array = re.split(fr"[,\n{self.separator}]",self.number_string)
            return number_array
        else:
            raise SeparatorsAtEndError
    
    def change_delimiter(self):
        return self.number_string.split("\n")[0][2:]
    
    def preprocess(self, number_array):
        valid_array = []  # List to hold valid non-negative integers
        negative_array = []  # List to hold any negative integers

        for number in number_array:
            try:
                int_num = int(number) # Try to convert the split string to an integer
                if(int_num>=0):
                    valid_array.append(int(number)) 
                else:
                    negative_array.append(int(number)) 

            except ValueError:
                # Ignore non-integer values
                continue
        return valid_array,negative_array


    def parse_array(self):
        """
        Parse the input string and return a list of valid non-negative integers.

        Raises:
            ValueError: If any negative numbers are found in the input string.
        """
        
        number_array = self.split_string()
        valid_array, negative_array = self.preprocess(number_array)
        

        # If there are negative numbers, raise a ValueError exception
        if(len(negative_array)>0):
            raise NegativeNumberError(negative_array)
        
        return valid_array 

class Sum:
    """Class responsible for calculating the sum of valid numbers."""

    def __init__(self, number_string="") -> None:
        self.number_string = number_string
        self.parser = Parser(self.number_string)  # Initialize the parser with the input string



    def another_sum(self):
        """
        Calculate the sum of valid numbers parsed from the input string.

        Returns:
            int: The total sum of valid non-negative integers.
        """
        if self.number_string == "":
            return 0
        valid_array = self.parser.parse_array() # Parse the numbers using the NumberParser

        return sum((x%1000) for x in valid_array) # Return the sum of valid numbers

    
    
    




    
    


