
class WhileLoop:

    _x = 0

    def _run_commands(self):
        print(self._x)
        self._x = self._x + 1        

    def test_do_while(self):    
        self._run_commands()
        while(self._x < 10):
            self._run_commands() 

    def single_line_while_stat(self):
        x = 1
        while(x <= 10): print(x)

    def continue_while_loop(self):
        x = 1
        while (x <= 10):            
            if(x == 5):
                x += 1                                
                continue                        
            else:                
                print(x)
                x += 1