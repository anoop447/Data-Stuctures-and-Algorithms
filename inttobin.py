
from stack import Stack

def intBin(decNum):

    s = Stack()
    while decNum > 0:
        r = decNum % 2
        s.push(r)
        decNum = decNum // 2
    
    binNum = ''
    while not s.isEmpty():
        
        binNum += str(s.remove())

    return binNum

print(intBin(242))
        
        
