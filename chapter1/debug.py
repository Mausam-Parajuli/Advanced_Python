import pdb

def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f

pdb.set_trace()

fact(5)
"""
alist = [1,2,3,4,5,6]

pdb.set_trace()

while(True):
    alist.pop()
    print(alist)

"""