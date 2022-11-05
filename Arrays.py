# Laboratory 2
# Angelica C. Delmendo
# BSCOE 2-2
# Arrays vs Variables

list1 = [4,7,8,3,0,1,90,34,2,6]
print(list1)
print("1-> Add an element")
print("2-> Insert an element")
print("3-> Modify an element")
print("4-> Delete an element")
print("5-> Arrange in ascending")
print("6-> Arrange in descending")
selection = int(input("What do you want to do in 1-6?"))
if selection ==1:
    print("Add an element")
    b=int(input("Enter an element: "))
    list1.append(b)
    print(list1)
elif selection ==2:
    print("Insert an element")
    b1 = int(input("Enter index: "))
    b2 = int(input("Enter an element: "))
    list1.insert(b1,b2)
    print(list1)
elif selection ==3:
    print("Modify an element")
    b1 = int(input("Enter index: "))
    b2 = int(input("Enter element: "))

    list1[b1] = b2
    print(list1)
elif selection ==4:
    print("Delete an element")
    b1 = int(input("Enter the index you want to delete: "))
    del list1[b1]
    print(list1)
elif selection ==5:
    print("Arrange in ascending order")
    list1.sort()
    print(list1)
elif selection ==6:
    print("Arrange in descending order")
    list1.sort(reverse=True)
    print(list1)
else:
    print("INVALID!")
