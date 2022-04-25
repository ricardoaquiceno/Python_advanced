def closure_str (string):
    def repeticiones(x):
        for i in range (1, x+1):
            print(string)
    return repeticiones
def main():
    first_word=closure_str(input("plbra a repetir "))
    first_word(int(input("ingrese el numero de repeticiones")))


if __name__=="__main__":
    main()