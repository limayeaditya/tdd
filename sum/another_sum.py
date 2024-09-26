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
        negative_array = []
        for number in number_array:
            try:
                int_num = int(number)
                if(int_num>=0):
                    valid_array.append(int(number))
                else:
                    negative_array.append(int(number))

            except ValueError as E:
                continue
        if(len(negative_array)>0):
            raise ValueError(f"negative numbers not allowed {[x for x in negative_array]}")
        return valid_array



    
    


