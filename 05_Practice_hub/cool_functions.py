# def hello(n):
#     print(f"Hello World number: {n}")

# for i in range(10):
#     hello(i)

# def rep_len(x = "default"):
#     for i in range(len(x)):
#         print(x)

# rep_len()
# rep_len("RIP")

# def sum_of_num(a , b):
#     return a+b

# print(f"sum of 2 , 5 is {sum_of_num(2 , 5)}")

# def how_many_time(word , charachter):
#     count = 0
#     for i in word:
#         if i == charachter:
#             count += 1
    
#     print(f"this word {word}, has {count} {charachter} charachter")

# how_many_time("Banana" , "a")

# def power_fun(number , p = 2):
#     cash = 1
#     for i in range(p):
#         cash = cash * number
    
#     return cash

# print(power_fun(2 , 10))

# def is_even(number):
#     cash = number%2 == 0
#     # if cash == True:
#     #     cash2 = "Even"
#     # else:
#     #     cash2 = "Odd"
#     # print(f"the number {number} is {cash2}")
#     # print(cash)
#     return cash

# # is_even(10)
# # is_even(11)
# # is_even(111)
# # is_even(112)
# def number_of_even(X):
#     count = 0
#     for i in X:
#         if is_even(i):
#             count += 1
#     return count
# numbers = [1 , 4 , 4 , 6, 7 ,9 , 12 , 2001 , 0 , 12]
# print(number_of_even(numbers))

# def largest_num(nums):
#     xlarge = nums[0]
#     for i in nums:
#         if xlarge < i :
#             xlarge = i
#     return xlarge

# print(f"{largest_num([2001.1 , 4 , 4 , 6, 7 ,9 , 12 , 2001 , 0 , 12])}")

# def plus_and_time(a , b):
#     return a+b , a*b # this will return a tuple

# print(plus_and_time(5 , 4))

# def is_greater(a , b):
#     return a>b

# print(is_greater(10 , 5))
# print(is_greater(5 , 10))
# print(is_greater(5 , 5))
# def is_even(n):
#     return n%2 == 0

# print(is_even(10))
# print(is_even(11))
# print(is_even(12))
# print(is_even(14))

# def zarb(*args):
#     print(args)
#     return args

# a = zarb(3 , 4 , 5)
# print(f"result value are: {a}")

# def sum_numbers(*args):
#     ss = 0
#     for i in args:
#         ss += i
#     return ss

# print(sum_numbers(1 , 2, 3, 4 , 5))

def pick_evens(*args):
    my_list = []
    for i in args:
        if i%2 == 0:
            my_list.append(i)
    return my_list

print(pick_evens(1))