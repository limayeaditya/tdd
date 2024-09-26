import pytest
from pytest import raises
from sum import another_sum

# add comments everywhere 

def test_another_sum_no_parameters():
    sum_ = another_sum.Sum()
    assert sum_.another_sum() == 0

def test_another_sum_one_parameter():
    sum_ = another_sum.Sum("1")
    assert sum_.another_sum() == 1

def test_another_sum_two_parameters():
   sum_ = another_sum.Sum("1,2")
   assert sum_.another_sum() == 3

def test_another_sum_multiple_parameters():
   sum_ = another_sum.Sum("1,2,5,4")
   assert sum_.another_sum() == 12

def test_another_sum_delimiter_variation1():
   sum_ = another_sum.Sum("1\n,2")
   assert sum_.another_sum() == 3

def test_another_sum_delimiter_variation2():
   sum_ = another_sum.Sum("1\n,2,3")
   assert sum_.another_sum() == 6

def test_another_sum_delimiter_variation3():
   sum_ = another_sum.Sum("//;\n1;2")
   assert sum_.another_sum() == 3

def test_another_sum_negative_numbers():
   sum_ = another_sum.Sum("-1,-2")
   with raises(ValueError) as value_error:
      sum_.another_sum()
   assert str(value_error.value) == "negative numbers not allowed [-1, -2]"
      
def test_another_sum_negative_numbers2():
   sum_ = another_sum.Sum("-1,-2,5")
   with raises(ValueError) as value_error:
      sum_.another_sum()
   assert str(value_error.value) == "negative numbers not allowed [-1, -2]"



   

