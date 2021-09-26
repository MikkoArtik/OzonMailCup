import json


def to_excel_format(num_val: int) -> str:
    first_letter_code = (num_val - 1) // 26
    second_letter_code = num_val % 26
    result = ''
    if first_letter_code:
        result += chr(64 + first_letter_code)

    if second_letter_code:
        result += chr(64 + second_letter_code)
    else:
        result += 'Z'
    return result


if __name__ == "__main__":
    input_str = input()
    number = int(input_str)

    answer = to_excel_format(number)

    print(json.dumps(answer))
