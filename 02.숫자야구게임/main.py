import random

numbers = []
number = str(random.randint(0, 9))

for i in range(3):
    while number in numbers:
        number = str(random.randint(0, 9))
    numbers.append(number)

success = False
print(numbers)

while success is False:
    count_strike = 0
    count_ball = 0
    num = str(input("숫자 3자리를 입력하세요 > "))
    if len(num) == 3:
        for i in range(0, 3):
            for j in range(0, 3):
                if num[i] == numbers[j] and i == j:
                    count_strike += 1
                elif num[i] == numbers[j] and i != j:
                    count_ball += 1
        if count_strike == 0 and count_ball == 0:
            print("3 아웃 !!")
        elif count_strike == len(num):
            success = True
        else:
            output = ""
            if count_strike > 0:
                output += "{} 스트라이크".format(count_strike)
            if count_ball > 0:
                output += " {} 볼".format(count_ball)
            print(output.strip())

print("게임 성공")


