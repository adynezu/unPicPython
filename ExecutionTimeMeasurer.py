import time
def ExecutionTimeMeasurer(my_func):
    a = time.time()
    my_func()
    b = time.time()
    print (b-a) #time to run
    
@ExecutionTimeMeasurer
def testFunction(x=14, y=19, z=5):
    return x**y**z
