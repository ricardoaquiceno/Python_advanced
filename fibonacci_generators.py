
from ast import Break


def fibogen (*arg):
    max=-1

    if bool(arg):
        max=arg[0]
    
    n1=0
    n2=1
    cont_max=0
   
    while True:
        if cont_max < max or  max==-1:
            yield n1
            aux= n1+n2
            n1, n2= n2, aux
            cont_max+=1
        else:
            break
            
           
                  
     

def main():
    fibonumbers=fibogen(5)
    for i in fibonumbers: #This case is to generate all the instances and get all the numbers one by one, an error will not be raised 
        print(i)
    
    #fibo=fibogen(10)
     #for i in range(1,100):  if I use it like this, it will break and the system will raise an error when there are no mor Yields  taking into account I passed a max number to the fibogen generator
     #   print(next(fibo))

  

if __name__=="__main__":
    main()

           


