from sys import maxsize

class LargestSumContiguousSubarray:
    """
    Write an efficient program to find the sum of contiguous subarray within 
    a one-dimensional array of numbers which has the largest sum.

    A = [-2,-3,4,-1,-2,1,5,-3]

    """

    def maxSubArraySum(self, a):   
        size = len(a) 
        max_so_far = -maxsize - 1
        max_ending_here = 0
        start = 0
        end = 0
        s = 0
    
        for i in range(0,size):     
            max_ending_here += a[i]     
            if max_so_far < max_ending_here: 
                max_so_far = max_ending_here 
                start = s 
                end = i 
    
            if max_ending_here < 0: 
                max_ending_here = 0
                s = i+1

        results = "subarray: {}\n".format(a[start:end+1])
        results += "indice inicio: {}\n".format(start)
        results += "indice fin: {}\n".format(end)
        "suma: {}".format(sum(a[start:end+1]))
        return results
        
    def test(self):
         A = [-2,-3,4,-1,-2,1,5,-3]

         print('Array original A: {}'.format(str(A)))
         print('Resultados:')
         print(self.maxSubArraySum(A))
