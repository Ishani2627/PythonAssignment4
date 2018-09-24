#Que1
print("to reverse a list")
myList = [1,2,3,4,5]
print("myList: ", myList)
myList.reverse()
print("reversed list :", myList)
print("\n")

#Que2
print("extract uppercase letters from a string")
myString = "HeLLo WorLd!!"
print(myString)
print("uppercase letters are:")
for i in myString:
    if(i.isupper()) == True:
        print("\t", i)    
print("\n")

#Que3
print("split the user input on commas and the values in a list")
myString = input("enter any string :")
myList = myString.split(',')
print("list formed is :", myList)
print("\n")

#Que4
print("to check whether the string is palindrome or not")
string = input("enter any string : ")
print(string)
x = string[-1::-1]
print(x)
if(string == x):
    print("string is palindrome")
else:
        print("string is not palindrome")
print("\n")

#Que5
print("deep copy and shallow copy")
import copy
list1 = [1,2,3,4,5]
list2 = copy.copy(list1)
print("original list :",list1)
print("shallow copied list :", list2)
list1.append([6,7])
print("\r")
print("AFTER MAKING CHANGES")
print("original list :", list1)
print("shallow copied list :", list2)

print("\r")
list3 = copy.deepcopy(list1)
print("AFTER MAKING CHANGES")
list1[3] = 789
print("original list :", list1)
print("deep copied list :", list3)
