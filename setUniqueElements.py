class setUniqueElements:
    _numbers = [1, 2, 2, 3, 3, 4, 4,4, 5]     

    def get_unique_elements(self):
        list_of_unique_numbers = []
        unique_numbers = set(self._numbers)
        for number in unique_numbers:
            list_of_unique_numbers.append(number)
        
        print(list_of_unique_numbers)

    def get_unique_elements2(self):        
        list_of_unique_numbers = list(set(self._numbers))                 
        print(list_of_unique_numbers)