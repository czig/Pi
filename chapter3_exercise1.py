# Chapter 3, Exercise 1
# Description: Quick input Exercise

prompt_text = "Enter a number: "
user_in = input(prompt_text)
user_num = int(user_in)

for i in range(1,10):
    print(i, " times ", user_num, " is ", i*user_num)

even = (user_num % 2) == 0
zero = user_num == 0

if even == True and zero == False:
    print(user_num, " is even")
elif even == True and zero == True:
    print(user_num, "is neither even nor odd")
else:
    print(user_num, " is odd")
