#List Creation - list is a heterogenius.......
# x1 = [10,20,30,hi,True];
# print(x1, type(x1))
#...............................................................

#Add value in list..........
# x1 = []
# user = int(input("How many value u want to enter "))
# for i in range(0,user,1):
#     value = eval(input("Enter any value "))
#     x1.append(value)
# print(x1)
#...............................................................

#Insert a specific value in a list........................
# x1 = [10,20,30,40]
# print("Original List", x1)
# x1.insert(1,555)
# print("After insert a value ",x1)
#.................................................................

#Find the length.............
# x1 = [10,20,30,40,50]
# length = len(x1)
# print("Length is ",length)
#..................................................................

#Search value in list...........
# x1 = [10,20,30,40,50]
# print(x1)
# no = int(input("Enter value you want to search "))
# c = x1.count(no)
# if c>0:
#     print("Found")
# else:
#     print("Not found")
#......................................................................

#Another way to search....
# x1 = [10,20,30,40,50]
# print(x1)
# no = int(input("Enter value you want to search "))
# c = x1.count(no)
# if no in x1:
#     print("Found")
# else:
#     print("Not found")
#.......................................................................

#Remove multiple value from the list..
# x1 = [10,20,30,20,40,10]
# print(x1)
# no = int(input("Enter value you want "))
# while True:
#     c = x1.count(no)
#     if c == 0:
#         break;
#     else:
#         x1.remove(no)
# print("After remove ",x1)
#.........................................................................

#Another method........
# x1 = [10,20,30,20,40,10]
# print(x1)
# no = int(input("Enter value you want "))
# while True:
#     if no in x1:
#         x1.remove(no)
#     else:
#         break;
# print("After remove ",x1)
#..........................................................................

#Rempve extra space at the time of input taken using strip
# city = input("Enter any city " )
# citylist = ["kol","del","mum","hyd"]
# if city in citylist:
#     print("Found")
# else:
#     print(city," Not Available")
#..........................................................................

#List Copy.....
# x1 = [50,15,25,5]
# x2 = x1
# print("X1 List ",x1)
# print("x2 list ",x2)
# x1.sort()
# print("x1 After sort ",x1)
# print("x2 list ",x2)
#..........................................................................

#Count number of words in a string...
# s1 = input("Enter any string ")
# x = s1.split()
# print(x, len(x))
#.........................................................................

#Search a word in a string
# s1 = input("Enter any string ")
# x = s1.split()
# w = input("Enter any word ")
# if w in s1:
#     print("Found")
# else:
#     print("Not found")
# print(x, len(x))
#..............................................................................

#Replace a word with another word is a string...
# s1 = input("Enter any string ")
# x = s1.split()
# w = input("Enter any word that u want to replace ")
# repword = input("Enter Replaced word ")
# if w in x:
#     for i in range(len(x)):
#         if x[i] == w:
#             x[i] = repword
#     s = ''
#     for i in range (len(x)):
#         s = s+x[i]+''
#         print(s)
# else:
#     print("Not found")
# print(x, len(x))
#.............................................................................

#Check 2 strings are anagram or not....
# READ   DEAR  this is called anagram....
# s1 = input("Enter a string ")
# s2 = input("Enter anagram of the string ")
# if(sorted(s1) == sorted(s2)):
#     print("The string is Anagram.")
# else:
#     print("The string is not anagram.")
#............................................................................

#