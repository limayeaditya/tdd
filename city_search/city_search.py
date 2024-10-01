cities = ["Paris","Budapest","Skopje","Rotterdam","Valencia","Vancouver","Amsterdam","Vienna","Sydney","New York City","London","Bangkok","Hong Kong","Dubai","Rome", "Istanbul"]
class Search:
    def __init__(self, search_string) -> None:
        self.search_string = search_string

    def check_search_string(self):
        if len(self.search_string)>=2:
            return True
        return False

    
    def search(self):
        result = []
        if not self.check_search_string():
            return ""
        for city in cities:
            if self.search_string.lower() in city.lower():
                result.append(city)
        return result