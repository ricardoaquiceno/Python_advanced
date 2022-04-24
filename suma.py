
def sum(a: int, b: int)-> int:
    return a+b

def main():
    x,y =input("Enter 2 numbers to sum " ).split()
    result= sum(x,y)
    print(type(result))
   
      

if __name__=="__main__":
    main()