def is_palindrome(string: str) -> bool:
    string = string.replace(' ', '').lower()
    return string == string[::-1]

def main():
    x=input("Please type your phrase " )
    if x.isnumeric(): #with this IF I force the input if it is a number to force the type and see the error, 
        x=int(x)      # That is the only purpose of this IF, force the Type error
    print(is_palindrome(x))

if __name__=="__main__":
    main()