class ValidationError(ValueError):
    def __init__(self, error_message_array) -> None:
        self.error_message_array = error_message_array
        if len(self.error_message_array)>1:
            super().__init__("\n".join(self.error_message_array))
        else:
            super().__init__(self.error_message_array[0])



class Validator:
    def __init__(self, password_string) -> None:
        self.password_string = password_string

    def validate(self):
        error_message = []

        if not self.atleast_eight_char():
            error_message.append("Password must be at least 8 characters")
        if not self.atleast_two_numbers():
            error_message.append("The password must contain at least 2 numbers")
        if not self.atleast_one_capital_letter():
            error_message.append("The password must contain at least one capital letter")
        if not self.atleast_one_special_char():
            error_message.append("The password must contain at least one special character")
        if len(error_message) == 0:
            return True
        else:
            raise ValidationError(error_message)

    def atleast_eight_char(self):
        if(len(self.password_string)< 8):
            return False
        else:
            return True
    
    def atleast_two_numbers(self):
        num_array = []
        for char in self.password_string:
            if char.isnumeric():
                num_array.append(char)
        if len(num_array)>=2:
            return True
        else:
            return False
    
    def atleast_one_capital_letter(self):
        for char in self.password_string:
            if char.isupper():
                return True
        return False
    
    def atleast_one_special_char(self):
        for char in self.password_string:
            if not char.isalnum():
                return True
        return False
        

class PasswordValidator:
    def __init__(self, password_string) -> None:
        self.password_string = password_string
    def validate(self):
        validate= Validator(self.password_string)
        return validate.validate()
            
        