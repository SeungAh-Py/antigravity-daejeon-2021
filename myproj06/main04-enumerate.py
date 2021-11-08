s = "안녕하세요."

idx = 0
for ch in s:
    print(idx, ch)
    idx += 1

for idx, ch in enumerate(s, 1):
    print(idx, ch)

# ...

numbers = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10],
]

for (x, y) in numbers:
    print(x, y)

for idx, (x, y) in enumerate(numbers):
    print(x, y)
