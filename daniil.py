from typing import List


def summ(x):
    res = 0

    for i in range(x, 7):
        res += i

    return res


def count(solution):
    def recursion(probability, s, mt):
        if (s == len(solution)):
            return probability * 3.5 + mt

        current_prpbability = (6 - (solution[s] - 1)) / 6

        mt += current_prpbability * probability * (summ(solution[s]) / (6 - (solution[s] - 1)))

        return recursion(probability - (probability * current_prpbability), s + 1, mt)

    return recursion(1, 0, 0)

solutions = [[1], [2], [3], [4], [5], [6]]

def paste(arr, x):
    res = []

    for i in range(len(arr)):
        res.append(arr[i])
    res.append(x)

    return res

def update(lst) -> List[List[int]]:
    res = []

    for i in range(1, 7):
        for j in range(len(lst)):
            res.append(paste(lst[j], i))

    return res

for i in range(1, 50):
    ans = 0
    nums = []

    for j in range(len(solutions)):
        if (count(solutions[j]) > ans):
            ans = count(solutions[j])
            nums = solutions[j]

    print(f"n = {i}, best M(x) = {round(ans, 4)} ", end="Items: ")
    print(*nums)

    solutions = update(solutions)



