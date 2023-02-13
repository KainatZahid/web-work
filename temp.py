#variable
a=30
print(a)
#Data types
a=71 #integer
b=1.2 #float
c="hello" #string
#TYPE CASTING
a=int(2.8) #output will be 2
b=float("4.2") #output will be 4.2
c=str("hello") #output will be hello
# string slicing
#start
b="hello , world!"
print(b[2:5])
#end slice
b="hello , world!"
print(b[2:])
#length function
a=("herry")
print(len(a))
#count function
c=("I LOVE pakistan.i blong to pakistan")
print(c.count("pakistan"))
#find function
c=("I LOVE pakistan.i blong to pakistan")
x=c.find("pakistan")
print(x)
#replace function
c=("I LOVE pakistan.i blong to pakistan")
x=c.replace("pakistan","India")
print(x)
# List Method
list=[1,4,6,7,8,4,9,10]
#sort function
list.sort()
print(list)
list=["kainat","malaika","rahmeen"]
list.reverse()
print(list)
list=["kainat","malaika","rahmeen"]
list.append("Nadia")
print(list)
list=["kainat","malaika","rahmeen"]
list.insert(2,"Nadia")
print(list)
list=["kainat","malaika","rahmeen"]
list.remove("kainat")
print(list)
# dictionay in python
dict={"kainat":"pari","malaika":"churail","rahmeen":"friend"}
print(dict)
dict={"kainat":"pari","malaika":"churail","rahmeen":"friend"}
print(dict["kainat"])

#operation on set
s={1,8,2,3}
print(len(s))
s={1,8,2,3}
#conditional statement
a=22
if(a>9):
    print("Greater")
else:
    print("less")
#LOOPS

#for loop
a=[1,7,8]
for item in a:
    print(a)
for i in range (0,7):
    print(i)
    a=[1,2,3]
    for item in a:
        print(a)
    else:
        print("Done")
for i in range(0,80):
    print(i)
    if i==3:
        break
    for i in range(4):
        print("hello")
        if i==2:
            continue
        print(i)




