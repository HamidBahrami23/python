#simple Calculator project
def add(x , y):
    return x + y
def sub(x , y):
    return x - y
def div(x , y):
    return x / y
def mul(x , y):
    return x * y


print("Welcome to Simple calculator Legend")
print("for exit write exit in any input")

while (True):
    while (True):
        x = input("tell me first number :")
        if x ==isinstance(x , int): break
        elif x == "exit": break
    z = input("what do you want? [ + , - , * , / ]    ")
    y = input("and what is the second number buddy?:")
    
    if x == "exit" or y == "exit" or z == "exit":
        break
    if z == "+":
        exp = add(x , y)
        print(f"ur number is : {exp}")
    elif z == "-":
        exp = sub(x , y)
        print(f"ur number is : {exp}")
    elif z == "/" and y != 0:
        exp = div(x , y)
        print(f"ur number is : {exp}")
    elif z == "*":
        exp = mul(x , y)
        print(f"ur number is : {exp}")
    else:
        print("Call Ambulance")

print("I use Arch BTW \n Have a nice day")

