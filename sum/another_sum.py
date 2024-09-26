import re


class Sum:
    def __init__(self, a="") -> None:
        self.a = a

    def another_sum(self):
        number_string = self.a
        if(number_string == ""):
            return 0
        
        number_array = re.split(r"[,;\n]",number_string)

        if(len(number_array)>0):
            total = sum([int(x) for x in number_array if x.isnumeric()])
            return total
    
            
    
    
    


