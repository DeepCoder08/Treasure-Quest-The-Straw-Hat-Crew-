class Stack:
    def __init__(self) -> None:
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
        self._Stacker= []
        
        
    def __len__(self):
        return len(self._Stacker)
        
        
    def is_empty(self):
        return len(self._Stacker)==0
        
        
    def pushdown(self, e):
        self._Stacker.append(e)
        
        
    def top(self):
        if self.is_empty():
            raise PathNotFoundException
        else: return self._Stacker[-1]
        
        
    def popup(self):
        if self.is_empty():
            raise PathNotFoundException
        return self._Stacker.pop()
        
        
        
    def inStacker(self,x,y):
        if((x,y) in self._Stacker):
            return True
        else:
            return False
            
    
    def display_Grid(self):
        for i in self._Stacker:
            print(i, end=' ')
        print()
        
    # You can implement this class however you like