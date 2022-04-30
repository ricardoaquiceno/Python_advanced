#DECORATORS: Decorators are functions that "decorate" another functio, they receive a function as parameter, add features 
# and return another fuction. 

from datetime import datetime #we are using this one to check the execution time

#this function below is a decorator, as it receives a function, and modifies it
def execution_time(func):
    def wrapper(*args,**kwargs): #this is called "wrapper" as its the part that wraps the function received with the new details
        initial_time=datetime.now()
        func(*args,**kwargs)
        final_time=datetime.now()
        time_elapsed= final_time - initial_time
        print("Pasaron "  + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper
#below is the wy to pass a function through a decorator to have the function modified and available to use
# later in the code
@execution_time
def test_func():
    for _ in range(1, 1000000):
        pass
@execution_time
def sum(a: int, b: int)->int:
    return a+b

if __name__=="__main__":
    test_func()
    sum(2,4)