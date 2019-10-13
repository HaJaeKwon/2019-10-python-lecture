import random
import os


def input_check(msg, casting=int):
    while True:
        try:
            user_input = casting(input("몇 일까요? "))
            return user_input
        except:
            continue


chance = 10
count = 0
min_number = 1
max_number = 99

number = random.randint(min_number, max_number)
os.system("clear")
print("{}부터 {}까지의 숫자를 {}번 안에 맞춰 보세요.".format(min_number, max_number, chance))

while count < chance:
    count += 1
    user_input = input_check("몇 일까요? ")
    if number == user_input:
        print("정답")
        break
    elif user_input < number:
        print("{} 보다 큰 숫자 입니다.".format(user_input))
    elif user_input > number:
        print("{} 보다 작은 숫자입니다.".format(user_input))


