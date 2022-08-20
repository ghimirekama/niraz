x = "aaviskar"
def myfunc():
    x= "niraz"
    print("bad"+x)
myfunc()
print(" bad"+x)


#list example
mylist = list(("kamal","aaviskar","dipesh"))
print(mylist)

mylist = ["apple","banana","cherry","mango","sugercane","kamal","hari"]
print(mylist)
print(mylist[0])
print(mylist[2:5])
print(len(mylist))
print(type(mylist))
print(mylist[2:])
print(mylist[:5])
print(mylist[-4:-1])
if "dipesh" not in mylist:
    print("yes ,'magno' is in the list ")
    list1=mylist.copy()
    print(list1)
    liststr=['a','b','c']
    listnum=[1,2,3]
    listnew=liststr+listnum
    print(listnew)
    mylist.clear()

#if else example
    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is greater than b")

        # while loop
