def gugudan(number):
    # number = 2
    print(f"--- {number}단 ---")
    for i in range(1, 10):
        print(f"{number} * {i} = {number * i}")


for number in range(2, 10):
    gugudan(number)
