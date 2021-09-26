from typing import List


def get_answer(arr: List[int]) -> int:
    arr.sort()
    result = 0
    for i in range(len(arr) // 2):
        result += arr[2 * i + 1] - arr[2 * i]
    return result


if __name__ == '__main__':
    amount = int(input())
    arr_data = list(map(int, input().split()[:amount]))
    print(get_answer(arr_data))
