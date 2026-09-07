

def compare_func(a , b , c):
    return a<b<=c

# print(compare_func(1 , 2 , 3))
# print(compare_func(1 , 2 , 2))
# print(compare_func(2 , 2 , 3))
# print(compare_func(2 , 2 , 1))

print("Welcome!")
a = input("Please insert your number 1: ")
b = input("Please insert your number 2: ")
c = input("Please insert your number 3: ")

print(f"The result is : {compare_func(a , b , c)}")