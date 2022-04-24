def prime(a: int)->bool:
    divisors= [ x for x in range(1,a+1) if a%x==0]
    
    if len(divisors)>2:
        return False
    else:
        return True
def main():
    x=input("please type a number to check if it is prime ")
    if x.isnumeric():
        x=int(x)
    print(prime(x))

if __name__=="__main__":
    main()