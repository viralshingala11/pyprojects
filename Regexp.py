import re                     #regular expression
txt="The first was alright, but was tough"
x=re.search("^The .*tough$",txt)      #^=start, .*endcharacter(if full stop also)$

print(x.start())
y=re.findall("was",txt)             # find particular character

z=re.search("\s",txt)             #  searches for space 

a=re.sub("\s"," second ",txt)        #can substitute anything in between spaces 


print(y)
print(z.start())
print(a)
if x:
    print("Yes")
else:
    print("no")

