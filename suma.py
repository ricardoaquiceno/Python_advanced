
# Need to check why this doesnt rise an error when used, should raise a problem when sending strings to a function set to be for 
#integers only 
def sum(a: int, b: int)-> int:
    return a+b

def main():
    x,y =input("Enter 2 numbers to sum separated by a space " ).split()
    result= sum(x,y)
    print(type(result))
     
if __name__=="__main__":
    main()