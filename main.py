#from methods_help import method_help
# from functions import welcome, add_numbers, num_dividedFrom_add_numbers, greet1, square
# from returnStuff import returnS, power, usd_to_eur

# from dynamic_functions import check_3Digits, all_positives
from function_interactions import mix_sticks, try_your_luck, verify_number

#method_help()
# function()
# welcome("Bob")
# added = add_numbers(4,5)
# print(added)
# final = num_dividedFrom_add_numbers(45, added)
# print(final)
# greet1()
# squared = square(5)
# print(squared)
# returnS()
# exponents = power(6,2)
# print(exponents)
# euro = usd_to_eur(10)
# print(euro)
# sum = 526 + 345

# result = check_3Digits([55, 99, 600, 8, 9457, 795])
# print(result)

# positives = all_positives([-55, 99, 600, 8, 9457])
# print(positives)
sticks = ["-","--","---","----","-----"]
my_mix = mix_sticks(sticks)
print(my_mix)


try1 = try_your_luck()
print(verify_number(my_mix,try1))