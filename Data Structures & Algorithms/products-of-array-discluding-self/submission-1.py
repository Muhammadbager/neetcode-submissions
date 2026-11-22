'''
INPUT:
nums - an integer array.

OUTPUT:
Return an array where each index contains the product
of all elements except the element at that index.

GOAL:
- Traverse the input array.
- Exclude the current element from its product.
- Calculate the product of the elements to the left.
- Calculate the product of the elements to the right.
- Combine both products for each index.
- Avoid using division.

EXAMPLE WALKTHROUGH 1:
nums = [2, 3, 4]

Index 0:
    Exclude 2.
    Multiply 3 * 4 = 12.

Index 1:
    Exclude 3.
    Multiply 2 * 4 = 8.

Index 2:
    Exclude 4.
    Multiply 2 * 3 = 6.

Output = [12, 8, 6]

EXAMPLE WALKTHROUGH 2:
nums = [2, 3, 4, 5]

Index 0:
    Left product = 1 (nothing on the left).
    Right product = 3 * 4 * 5 = 60.
    Result = 60.

Index 1:
    Left product = 2.
    Right product = 4 * 5 = 20.
    Result = 40.

Index 2:
    Left product = 2 * 3 = 6.
    Right product = 5.
    Result = 30.

Index 3:
    Left product = 2 * 3 * 4 = 24.
    Right product = 1 (nothing on the right).
    Result = 24.

Output = [60, 40, 30, 24]

EXAMPLE WALKTHROUGH 3 — EDGE CASE:
nums = [1, 0, 3]

Index 0:
    Exclude 1.
    Product = 0 * 3 = 0.

Index 1:
    Exclude 0.
    Product = 1 * 3 = 3.

Index 2:
    Exclude 3.
    Product = 1 * 0 = 0.

Output = [0, 3, 0]

PSEUDOCODE:
- Create a result array initialized with 1s.

- Initialize prefix product to 1.

- Traverse the array from left to right.
    - Store the current prefix product at the current index.
    - Multiply the prefix product by the current number.

- Initialize postfix product to 1.

- Traverse the array from right to left.
    - Multiply the result at the current index by the postfix product.
    - Multiply the postfix product by the current number.

- Return the result array.
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res