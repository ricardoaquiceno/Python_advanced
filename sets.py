#SETS: Are an unsorted collection of unique and immutable elements.
#Here you will find how to declare them and operate with them. 

if __name__=="__main__":
    my_set= {3,4,5} #this creates a normal set 
    print(my_set)
    my_set2 = {"hey", 34.5, False, 3}  #this creates also a normal set but with diferent variables
    print(my_set2)
    """ Taking into account the definition of sets, my_set3 creates a set which results
        must be {3,2} as sets do not repeat values"""
    my_set3={3,3,2,2} 
    print(my_set3)
    """ finally, this one below is an example of a wrong declared set that will raise an error
    the reason is that the list [1,2,3] is mutable, therefore, raising an error, it ca be uncomented to test"""
    # my_set4 = {[1,2,3], 4}
    # print(my_set4)
    """DECLARE EMPTY SETS: If one wants to declare an empty set, one must use the built in function set()
    otherwise, if we use empty curly braces "{}" python will think this is a Dictionary """
    empty_set=set()
    print(type(empty_set))
    empty_dict={}
    print(type(empty_dict))
    """CAST OBJECTS TO SETS: One can also create sets from other objects, we know this as casting, in order to cast one can use the
       built in function set() and provide as variable the onject one wants to cast"""
    my_list = [1,2,3,4,4,5]
    my_set_from_list=set(my_list)
    print(my_set_from_list)

    my_tuple = ("hey", "hey", "you", "you", 1 )
    my_set_from_tuple=set(my_tuple)
    print(my_set_from_tuple)

    """ HOW TO ADD ELEMENTS TO A SET: to add individual elements one should use .add() on the other hand if one wants
        to add multiple elements, one should use the method .update()"""
    print(my_set)
    my_set.add(89) #this one is to add individual elements, it cannot receive multiple elements separated by coma or lists 
    print(my_set)
    my_set.update([1,2,5,6])
    print(my_set)
    my_set.update({2,65},[22,90])
    print(my_set)

    """How to delete elements from a set? you can use .remove() or .discard() to delete elements, both have different ussages 
        and .remore() is more strict, also you can remove random elements with .pop() and leave the list empty with .clear()"""

    my_set.discard(1)
    print(my_set)
    my_set.remove(65)
    print(my_set)
    my_set.discard("hola") #Discard does not generate error when you try to discard an element that does not exist
    print(my_set)
    """on the other hand, if one uses .remove() with an elemnt that does not exist, it raises an error, you can uncoment to try"""
    # my_set.remove("hola") 
    my_set.pop()
    print(my_set)
    my_set.clear()
    print(my_set)
    