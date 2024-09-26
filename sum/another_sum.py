import re


class Sum:
    def __init__(self, a="") -> None:
        self.a = a

    def another_sum(self):
        valid_array = self.filter_array()
        if(len(valid_array)>0):
            total = sum(valid_array)
            return int(total)
        return 0
    
    def filter_array(self):
        number_array = re.split(r"[,;\n]",self.a)
        valid_array = []
        for number in number_array:
            if number.isnumeric():
                valid_array.append(int(number))
        return valid_array



    
    


