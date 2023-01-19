#there is no need to init. type of variab.
a=5
name="Aidyn"
#if we write new meaning to var
name=5
#it will input lates
print(name)
#also we can specify datatype
x=float(5)

#for example x now is "5"
x=str(5)
print(x)
#we can get type
print(type(x))

#about quotes the " " and '' same and youuse it when
print('i "love" coding')

A="Jake"
a="Sully"
#they not same

#about names of variables
"""
it starts from a-z or _ only
it can consist from A-z, 0-9 and _
"""
_pythonchik = 1
cppshka_ = 2
print("python eto nomer", _pythonchik, "cppshka eto", cppshka_, end='\n')

#we can use multiple values
x, y, z= "KBTU", "AITU", "IITU"
print(x, y, z, "topchiki")

#also we can use collections
topchiks=["KBTU", "SDU", "IITU"]
a, b, c=topchiks
print(a)
print(b)
print(c)

#in general print() used to output
print(5+6, "is summ of 5 and 6")

#we can create glob. var. to use it in functions
pi=3.14

def myFunc():
    print("S of krug with radius 3 is", 2*pi*3)
myFunc()



