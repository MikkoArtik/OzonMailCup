from math import log10 as lg


def get_answer(num: int) -> bool:
    while True:
        nums_count = int(lg(num)) + 1
        part_num = int(''.join(('1' for _ in range(nums_count))))
        if part_num > num or num < 11:
            return False
        elif part_num == num:
            return True
        else:
            num -= part_num


if __name__ == '__main__':
    test_count = int(input())
    for _ in range(test_count):
        is_good_num = get_answer(int(input()))
        result = 'YES' if is_good_num else 'NO'
        print(result)
