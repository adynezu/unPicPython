from urllib.request import urlopen

def rmiRpc(myFunc):
    html = urlopen("http://www.google.com/")
    print(html.read())
    myFunctionRead = urlopen(myFunc())
    print (myFunctionRead.read())

@rmiRpc
def testFunction(fb = "http://bigfoot.cs.upt.ro/~chirila/teaching/upt/cti22-paa/index.html"):
    return fb
