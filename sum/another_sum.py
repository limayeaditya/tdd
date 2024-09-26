import re

class Parser:
    """Class responsible for parsing and validating numbers from an input string."""

    def __init__(self, number_string="") -> None:
        self.number_string = number_string

    def split_string(self):
        # Split the input string using commas, semicolons, or newlines as delimiters
        number_array = re.split(r"[,;\n]",self.number_string)
        return number_array
    
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
            raise ValueError(f"negative numbers not allowed {[x for x in negative_array]}")
        
        return valid_array 

class Sum:
    """Class responsible for calculating the sum of valid numbers."""

    def __init__(self, number_string="") -> None:
        self.parser = Parser(number_string)  # Initialize the parser with the input string

    def another_sum(self):
        """
        Calculate the sum of valid numbers parsed from the input string.

        Returns:
            int: The total sum of valid non-negative integers.
        """
        
        valid_array = self.parser.parse_array() # Parse the numbers using the NumberParser

        return sum(valid_array) # Return the sum of valid numbers

    
    
    




    
    


