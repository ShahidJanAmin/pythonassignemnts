# task 1
Try = "Yes"
while Try !="Y":
    n1 = int(input("Enter the number: "))
    
    op = input("Enter the operation: ")
    n2 = int(input("Enter the another number: "))
    if op =="+":
        print("The Answer is =",n1+n2)
    elif op =="-":
        print("The Answer is =", n1-n2)
    elif op == "/":
        print("The Answer is =", n1/n2)
    elif op == "*":
        print("The Answer is =", n1*n2)
    elif op == "^":
        print("The answer is = ", n1**n2)
    else:
        print("Wrong choice try again")

    Try = input("Try another Y/N : \t").lower()



'''


#Task 2
List = ['a', 2,5, 'b', 55, 'd']

for item in List:
    if type(item) == int:
        print(item, "is interger and present in the list")


#Task 3
Dictionary = {'RAM':'Random Access Memory',
              'CPY':'Center Processing Unit'}
key = input("Enter the Key to add to Dictionary :")
value = input(f"Enter the value of {key} : ")
Dictionary[key] = value
print('the key and value is added in the dictionary')
print(Dictionary)


Disc = {44:'1st', '2nd':53, 23:'2r3'}
Sum =0
for i in Disc:
    if type(i)==int:
        Sum+=i

print("The sum of the numeric values of the Disctionary : ", Sum)

# Task 5
a = [1,2,34,5,2,5]
dublicated_values= []
for i in a:
    if a.count(i) >=2:
        if i not in dublicated_values:
            dublicated_values.append(i)

print("The values are present twice in the list")
print(dublicated_values)



# Task 6
Disc = {'RAM':'Random Access Memory',
              'CPY':'Center Processing Unit'}
key = input("Enter the Key to add to Dictionary :")
value = input(f"Enter the value of {key} : ")
if key in Disc:
    print(f"The {key} is also present in the Disctionary")
else:
    Disc[key] = value
    print("Added to the Disctionary")


'''
