
class fibonacci:
    """this class emulates the fibonacci series with an iterator"""
    def __init__(self,items=None):
        self.items=items
        self.iterations=0
        self.first=0
        self.second=1

    def __iter__(self):
        return self

    def __next__(self):
        if not self.items or self.iterations < self.items: # this limits the number of items to the number requested by the user
            first_one=self.first
            self.second=self.first+self.second
            self.first= self.second-first_one
            self.iterations+=1
            return first_one
        else:
            raise StopIteration
def main():
    fibo=fibonacci(10) 
    #for i in range(1,100):  if I use it like this, it will raise an error when the iterator meets the "max" taking into account I passed a max number to the Fibonassi iterator
     #   print(next(fibo))
    for i in fibo: 
        print(i)

if __name__=="__main__":
    main()