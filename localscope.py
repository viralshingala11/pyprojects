#local scope
"""def myfn():
    x=2
    print(x)
myfn()"""

#global scope
x=2
y=6
def myfn():
    x=30
    print(x)
myfn()
print(y)