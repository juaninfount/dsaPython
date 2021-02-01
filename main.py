from ArrayContainsArray import ArrayContainsArray
from LargestSumContiguousSubarray import  LargestSumContiguousSubarray 
from keywords import Keywords
from WhileLoop import WhileLoop
from Sleep import Sleep
from setUniqueElements import setUniqueElements
from LinearSearch import LinearSearch
from quicksort import Quicksort
from binarySearch import BinarySearch

if __name__ == "__main__":

    # check if array is duplicated within distance k
    # testcase = ArrayContainsArray()
    # testcase.test()    

    # testcase = LargestSumContiguousSubarray()
    # testcase.test()    

    #testcase = Keywords()
    #testcase.testCaseAssertKeyword()

    #testcase = WhileLoop()
    #testcase.continue_while_loop()

    #testcase = Sleep()
    #testcase.user_experience()
    #testcase.test_timestamp()

    # testcase = setUniqueElements()
    # testcase.get_unique_elements2()

    #testcase = LinearSearch()
    #testcase.test([1, 10, 30, 15,9,3,19],21)
    #testcase.test([88, 10, 67, 15,9,3,19],19)

    #testcase = Quicksort()
    # arr = [10, 30, 40, 50, 70, 90, 80]
    # testcase.quicksort(arr, 0, len(arr)-1)
    # print(arr)

    arr = [72,2,91,5,8,12,23,16,38,56]    
    testcase = BinarySearch(arr)
    index = testcase.binarySearch(arr, 0, len(arr)-1, 22)
    print('Posición de {} está localizado en el índice {}.'.format(23,index))

    
    
    

    
