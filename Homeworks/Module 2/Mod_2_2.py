first = int(input("Please, pick the first number: "))
second = int(input("Please, pick the second number: "))
third = int(input("Please, pick the third number: "))
if first == second and second == third and first == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)