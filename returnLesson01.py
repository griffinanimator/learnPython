""" Define a function to collect some information """
def getInfo():
    info = ('a', 'b')
    """ Return that information so we can use it in another function """
    return info

""" Define a function to print information.  Provide myInfo as an argument """   
def printInfo(myInfo):
    print "here is the info"
    print myInfo


""" myInfo will store the data we get from getInfo() """   
myInfo = getInfo()

""" Call printInfo() passing myInfo as an argument """
printInfo(myInfo)