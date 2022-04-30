def remove_duplicates(in_list):
    return list(set(in_list))
def main():
    my_list=[1,1,1,2,3,3,2,1,4,5,5]
    print(my_list)
    print(remove_duplicates(my_list))

if __name__=="__main__":
    main()