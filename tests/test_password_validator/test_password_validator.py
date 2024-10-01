import pytest
from pytest import raises
import password_validator.password_validator as PwdValidator 

def test_atleast_eight_char_negative():
   validator = PwdValidator.PasswordValidator("11A@a")
   with raises(ValueError) as LengthError:
      validator.validate()
   assert str(LengthError.value) == "Password must be at least 8 characters"  

def test_atleast_two_numeric_negative():
   validator = PwdValidator.PasswordValidator("abcde@fghiA")
   with raises(ValueError) as LengthError:
      validator.validate()
   assert str(LengthError.value) == "The password must contain at least 2 numbers" 


def test_atleast_two_numeric_and_eight_chars_negative():
   validator = PwdValidator.PasswordValidator("ab2R@")
   with raises(ValueError) as LengthError:
      validator.validate()
   assert str(LengthError.value) == "Password must be at least 8 characters\nThe password must contain at least 2 numbers" 

def test_atleast_one_capital_letter_negative():
   validator = PwdValidator.PasswordValidator("abcdef@gij22")
   with raises(ValueError) as LengthError:
         validator.validate()
   assert str(LengthError.value) == "The password must contain at least one capital letter" 

def test_atleast_one_special_char_negative():
   validator = PwdValidator.PasswordValidator("abcdefgRij22")
   with raises(ValueError) as LengthError:
         validator.validate()
   assert str(LengthError.value) == "The password must contain at least one special character" 
   

    