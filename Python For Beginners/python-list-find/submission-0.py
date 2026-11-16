from typing import List # this is used to add type hints for List type

def find_index(nums: List[int], target: int) -> int:
    total = 0
    for num in nums:
        if target == num:
            return total
        total += 1
    return 0


# don't modify code below this line
print(find_index([1, 2, 3, 4, 5], 3))
print(find_index([1, 2, 3, 4, 5, 3], 3))
print(find_index([1, 2, 3, 4], 1))
print(find_index([1, 3, 4, 2], 2))

