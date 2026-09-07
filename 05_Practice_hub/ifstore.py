def total_price(input):
    if input >= 50000 :
        return 0.8 * input
    elif 20000 < input< 50000:
        return 0.9 * input
    else:
        return input

x = [ 15000 , 20000 , 30000 , 50000 , 55000]

for i in x:
    print(f"the result of {i} is: {total_price(i)}")