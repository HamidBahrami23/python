def donation_info(don_dic):
    def is_even(number):
        return number % 2 == 0 
    total = 0
    maximum = -1
    name_max = ""
    for na ,  n in don_dic.items():
        total += n 
        if maximum < n:
            maximum = n
            name_max = na
    average = total / len(don_dic)
    if  is_even(maximum):
        even_max = "even"
    else:
        even_max = "odd"
    return maximum , name_max , average , len(don_dic) , even_max


donations = {
        "Jon": 5,
        "Katty": 1.25,
        "Linus": 7,
        "Bill": 0.2 ,
        "Elon": 1.3
        }

max_don , max_don_name , avg , numbers , is_even = donation_info(donations)
print(f"our maximum donation was {max_don}$, thanks to {max_don_name} , ur donation is {is_even} number")
print(f"average donation was: {avg}")
print(f"number of donation was: {numbers}")




