from typing import List


def is_tag(line):
    return line[0] == '<' and line[-1] == '>'


def is_open_tag(tag):
    if len(tag) == 2:
        return True
    else:
        return tag[1] != '/'


def create_anti_tag(tag):
    if is_open_tag(tag):
        return '</' + tag[1:]
    else:
        return '<' + tag[2:]


def strip_tag(tag):
    return tag[1:-1].upper()


def load_test_cases():
    result = []
    with open('./cases/task_b.txt', 'r') as f:
        test_count = int(f.readline().rstrip())
        for _ in range(test_count):
            lines_count = int(f.readline().rstrip())
            case = []
            for _ in range(lines_count):
                line = f.readline().rstrip().lower()
                if is_tag(line):
                    case.append(line)
            result.append(case)
    return result


def get_result(arr: List[str]):
    open_tags = []
    closed_tags = []
    for tag in arr:
        if is_open_tag(tag):
            open_tags.append(tag)
        else:
            if len(open_tags) == 0:
                closed_tags.append(tag)
            else:
                if open_tags[-1] == create_anti_tag(tag):
                    open_tags.pop()
                else:
                    closed_tags.append(tag)

    if len(closed_tags) + len(open_tags) == 0:
        return 'CORRECT'
    elif len(closed_tags) + len(open_tags) == 1:
        if len(closed_tags):
            return f'ALMOST {strip_tag(closed_tags[0])}'
        else:
            return f'ALMOST {strip_tag(open_tags[0])}'
    elif len(closed_tags) + len(open_tags) == 3:
        if len(closed_tags) == 0 or len(open_tags) == 0:
            return 'INCORRECT'
        else:
            if open_tags[0] == create_anti_tag(closed_tags[-1]):
                if len(open_tags) == 2:
                    return f'ALMOST {strip_tag(open_tags[-1])}'
                else:
                    return f'ALMOST {strip_tag(closed_tags[0])}'
            else:
                return 'INCORRECT'
    else:
        return 'INCORRECT'


def context_cmd():
    test_count = int(input())
    for _ in range(test_count):
        lines_count = int(input())
        case = []
        for _ in range(lines_count):
            line = input().lower()
            if is_tag(line):
                case.append(line)
        print(get_result(case))


def test_cases():
    for case in load_test_cases():
        result = get_result(case)
        print(result)


if __name__ == '__main__':
    context_cmd()
