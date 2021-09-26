

def get_answer(amount: int, length: int):
    if amount >= length:
        return 1
    else:
        if length % amount:
            return int(length / amount) + 1
        else:
            return int(length / amount)


if __name__ == '__main__':
    current_amount, current_length = map(int, input().split())
    print(get_answer(current_amount, current_length))
