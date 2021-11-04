# def number_return(number):
#     return (number // 1000) * 1000


# number = int(input("1000이상의 숫자를 입력하세요 : "))
# print(number_return(number))

# 문자열을 인자로 받아 공백을 제외한 글자를 반환하는 함수

# 전역변수 (global variable) => 최소화
# acc = []


def get_count(s):
    acc = []  # 지역변수 (local variable)

    for i in s:
        if i != " ":
            acc.append(i)
    return len(acc)


sentence = "우리는 파이썬을 즐겨요"
print(get_count(sentence))
print(get_count(sentence))
