from quicksort import Quicksort 

class BinarySearch:
    
    def binarySearch(self, arr, l, r, x):       
        if l <= r:
            mid = (l + r)//2            
            if arr[mid] == x:
                return mid
            elif  x < arr[mid]:
                return self.binarySearch(arr,l,mid-1,x)
            else:
                return self.binarySearch(arr,mid+1,r,x)
        else:
            return -1
        
    def __init__(self,arr):
        testcase = Quicksort()
        testcase.quicksort(arr, 0, len(arr)-1)

        super().__init__()