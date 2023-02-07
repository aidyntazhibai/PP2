#list act like array
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#also we can replace them
fruits = ["apple", "banana", "cherry"]
fruits[0]= "kiwi"

#append method add new item (last)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#insert method add item into specified index
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

#remove
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#del and popalso removes items

fruits.pop(1)
del fruits[0]

#without indexes

fruits = ["apple", "banana", "cherry"]

fruits.pop()  #remove last one
del fruits    #delete entire list

#clear method
fruits = ["apple", "banana", "cherry"]
fruits.clear()    #it remains list but clears it


#negative indexing (-1 refers to the last item)
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#printing range of items (first included last not)
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])