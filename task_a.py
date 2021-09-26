from typing import List


def create_tree(levels: List[List[int]]):
    top_level = levels[0]
    for level_index in range(1, len(levels)):
        new_level = [0] * (level_index + 1)
        for i in range(level_index + 1):
            left_root, right_root = i - 1, i
            if left_root >= 0:
                new_level[i] = levels[level_index][i] + top_level[left_root]
            if right_root < len(top_level):
                new_level[i] = levels[level_index][i] + top_level[right_root]
        top_level = new_level
    print(top_level)

    for item in levels:
        print(item)


a= [[5], [-2, 3], [0, -7, 1]]
create_tree(a)