class Quicksort:

    def __partition(self, arr, low, high):
        i = (low-1)
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] < pivot:
                i = i+1
                arr[i],arr[j] = arr[j],arr[i] 

        arr[i+1],arr[high] = arr[high],arr[i+1]
        return (i+1)

    # The main function that implements Quicksort
    # arr[] --> Array to be sorted
    # low   --> Starting index
    # high  --> Ending index
    def quicksort(self, arr, low, high):
        if low < high:
            pi = self.__partition(arr, low, high)

            self.quicksort(arr, low, pi-1)
            self.quicksort(arr, pi+1, high)

    def __init__(self):
        super().__init__()