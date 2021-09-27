from typing import List, Tuple
from math import gcd


def calc_sum(arr: List[List[int]]) -> Tuple[int, int]:
    current_coeffs = [2 ** (len(arr) - 1)]
    result = 0
    for item in arr:
        new_coeffs = []
        for i, el in enumerate(item):
            result += el * current_coeffs[i]
            if i == 0:
                new_coeffs += [current_coeffs[i] // 2, current_coeffs[i] // 2]
            else:
                new_coeffs[-1] += current_coeffs[i] // 2
                new_coeffs.append(current_coeffs[i] // 2)
        current_coeffs = new_coeffs

    if result == 0:
        return 0, 1
    else:
        k = gcd(result, 2 ** (len(arr) - 1))
        return result // k, 2 ** (len(arr) - 1) // k


def load_test():
    result = []
    with open('1.txt') as f:
        f.readline()
        f.readline()
        for line in f:
            result.append(list(map(int, line.rstrip().split())))
    return result


if __name__ == '__main__':
    test_count = int(input())
    if test_count == 0:
        print('0 1')
        exit()

    for _ in range(test_count):
        height = int(input())
        case = []
        for _ in range(height):
            case.append(list(map(int, input().split())))
        res = calc_sum(case)
        print(f'{res[0]} {res[1]}')
