class LinearSearch:
    def search(self, arr, x):
        for index, value in enumerate(arr):
            if value == x:
                return index
        return -1

    def test(self, arr, x):
        print( '{} is present at index {}'.format(x , self.search(arr,x) ) )