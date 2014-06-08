def Logger(my_func):
    print my_func.__name__ #Numele functiei
    print my_func() #Un tuplu de argumente
    
@Logger
def testFunction(x=85, y=11, z="abc!"):
    return x,y,z
