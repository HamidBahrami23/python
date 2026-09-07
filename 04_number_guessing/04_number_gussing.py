import random

def welcome():
    print("Welcome ...")
    print("guess the number in [1 , 100] and you will be legend")

def get_input():
    return int(input("please insert the number you guessed: "))

def comparef(num , gue):
    if gue > num:
        return "your number is big" , True
    elif gue < num:
        return "your number is small" , True
    return "you goddamn right , Your Legend" , False

def do_you():
    while True :
        x = input("Do you want to continue? [Y/n]")
        if x.upper() == "Y":
            return True
        elif x.upper() == "N":
            return False
        else :
            print("insert right arguments Y for yes and N for no")


go_on = True
round = 0

welcome()

while (go_on == True):
    round += 1
    count = 0
    print(f"Round {round} Started!")
    the_number = random.randint(1 , 100)

    keep_going = True
    while keep_going == True :
        count += 1
        guess = get_input()

        txt , keep_going = comparef(the_number , guess)
        print(txt)

    print(f"round {round} , number of trys: {count}")
    go_on = do_you()

print("Fare well!")