import city_search.city_search as CitySearchModule
def test_less_than_two_char_negative():
    city = CitySearchModule.Search("A")
    result = city.search()
    assert result == ""

def test_exact_city_search_string_positive():
    city = CitySearchModule.Search("Va")
    result = city.search()
    assert result == ["Valencia", "Vancouver"]
    

def test_case_insensitive_positive():
    city = CitySearchModule.Search("va")
    result = city.search()
    assert result == ["Valencia", "Vancouver"]
   
def test_substring_of_city_name():
    city = CitySearchModule.Search("cou")
    result = city.search()
    assert result == ["Vancouver"]