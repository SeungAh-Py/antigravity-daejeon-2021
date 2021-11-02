answer = input("12 + 23 = ")

# answer를 가지고 계산할 목적이라면,
# answer 값 변환은 최대한 빠르게 수행하는 것이 좋습니다.
answer = int(answer or 0)

# if len(answer) == 0:
#     answer = 0
# else:
#     answer = int(answer)

if answer == 35:
    print("정답")
else:
    print("땡!!!")
