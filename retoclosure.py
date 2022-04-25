def make_div_by(n): 
    def num_to_divide(num):
        assert n !=0, "division by zero is not defined"
        return num/n
    return num_to_divide

def main():
    divide_3=make_div_by(3)
    divide_5=make_div_by(5)
    divide_18=make_div_by(18)
    print(divide_3(18))
    print(divide_5(100))
    print(divide_18(54))
if __name__=="__main__":
    main()