class ArrayContainsArray:
    
    """ 
    Input: k = 3, arr[] = {1, 2, 3, 4, 1, 2, 3, 4}
    Output: false
    All duplicates are more than k distance away.
    Existen duplicados a una distancia mayor a k posiciones

    Input: k = 3, arr[] = {1, 2, 3, 1, 4, 5}
    Output: true
    1 is repeated at distance 3.

    Input: k = 3, arr[] = {1, 2, 2, 4, 5}
    Output: false

    Input: k = 3, arr[] = {1, 2, 3, 4, 4}
    Output: true
    """
    
    def _checkDuplicatesWithinK(self, arr, n, k):
        myset = []
        for i in range(n):
            if arr[i] in myset:
                return True

            myset.append(arr[i])

            if (i >= k): 
                myset.remove(arr[i - k]) 

        return False    

    def test(self):
        arr =  [1, 2, 2, 4, 5]
        k = int(input("Ingresar distancia k: ")) 
        n = len(arr)

        while k >= n:
            if k >= n:
                k = int(input("k < SizeArray. Ingresar distancia k: ") ) 
         
        print(self._checkDuplicatesWithinK(arr, n , k))
    
    