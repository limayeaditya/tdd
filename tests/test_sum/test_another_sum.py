import pytest
from pytest import raises
from sum import another_sum

# Each test case checks different scenarios for summing numbers with varying inputs and delimiters.

# Test case 1: No parameters passed, expecting sum to be 0
def test_another_sum_no_parameters():
    sum_ = another_sum.Sum()  
    assert sum_.another_sum() == 0  

# Test case 2: Single valid number passed, expecting sum to be equal to the number
def test_another_sum_one_parameter():
    sum_ = another_sum.Sum("1")  
    assert sum_.another_sum() == 1  

# Test case 3: Two valid numbers passed, expecting sum of the two
def test_another_sum_two_parameters():
   sum_ = another_sum.Sum("1,2")  
   assert sum_.another_sum() == 3  

# Test case 4: Multiple numbers passed, expecting their sum
def test_another_sum_multiple_parameters():
   sum_ = another_sum.Sum("1,2,5,4") 
   assert sum_.another_sum() == 12  

# Test case 5: Variation of delimiters (comma and newline), expecting correct sum
def test_another_sum_delimiter_variation1():
   sum_ = another_sum.Sum("1\n,2") 
   assert sum_.another_sum() == 3  

# Test case 6: Another variation of delimiters with additional numbers
def test_another_sum_delimiter_variation2():
   sum_ = another_sum.Sum("1\n,2,3")  
   assert sum_.another_sum() == 6  

# Test case 7: Custom delimiter definition "//;" and numbers separated by semicolon
def test_another_sum_delimiter_variation3():
   sum_ = another_sum.Sum("//;\n1;2")  
   assert sum_.another_sum() == 3  

# Test case 8: Handling negative numbers - expecting a ValueError
def test_another_sum_negative_numbers():
   sum_ = another_sum.Sum("-1,-2")  
   with raises(ValueError) as value_error:  
      sum_.another_sum()
   assert str(value_error.value) == "negative numbers not allowed [-1, -2]"  

# Test case 9: Handling mixed positive and negative numbers - expecting a ValueError
def test_another_sum_negative_numbers2():
   sum_ = another_sum.Sum("-1,-2,5")  
   with raises(ValueError) as value_error:  
      sum_.another_sum()
   assert str(value_error.value) == "negative numbers not allowed [-1, -2]"  
