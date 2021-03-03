class A:
    def __init__(x,y,z):
        x.firstvalue=y
        x.secondvalue=z
obj = A(5,78)
print(obj.firstvalue)
print(obj.secondvalue)