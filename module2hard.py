import itertools
n = int(input("Введите число от 3 до 20: "))
pairs = list(itertools.combinations(range(1, n), 2))
result = ""
for pair in pairs:
    if n % sum(pair) == 0:
        result += str(pair[0]) + str(pair[1])

print(result)