
class Keywords:

    def testCaseAssertKeyword(self):
        mark2 = [55,88,78,90,79]        
        #mark2 = []
        myavg = self._avg(mark2)
        print("Average of mark2: {0:.2f}".format(myavg))
        

    def _avg(self,marks):
        assert len(marks) != 0, "List is empty"
        return sum(marks)/(len(marks))
         