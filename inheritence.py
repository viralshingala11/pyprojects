class A:                     # parent class
    def __init__(a,x,y):
        a.fname = x                 #setting x and y with help of "a"
                                       # so "a" basically sets the value with name as fname. 
        a.mname = y 
        
    def myfunc(a):
        print(a.fname,a.mname)
        
class B(A):                   # child class and to access parent class we put
                               # B(A) to get access
    def __init__(a,x,y):
        super().__init__(x,y)           # to get particular parameter
        a.lname = "ghi"

n=B("abc","def")                   #declaring new variable to assign arguments to 
                                   # parent class parameters defined as above
n.myfunc()
print(n.lname)



