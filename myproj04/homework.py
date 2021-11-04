for number in range(3, 10, 3):
    for i in range(1, 10):
        print(f"{number} * {i} = {number * i}")

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

for i in range(1, 100):
    if i % 15 == 0:
        print(i)

for i in range(15, 100, 15):
    print(i)

acc = 0
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        acc += i
print(acc)

number_list = []
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        number_list.append(i)
print(sum(number_list))

for number in range(2, 10):
    for i in range(1, 10):
        if i <= number:
            print(f"{number} * {i} = {number * i}")

for number in range(2, 10):
    for i in range(1, number + 1):
        print(f"{number} * {i} = {number * i}")
