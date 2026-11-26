class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        Input:
            heights - array of integers
            heights[i] - height of the bar
            width of each bar is 1
        output:
            return the area of the largest rectangle that can be made
        
        Approach one
        I can store the min height in a stack
        Then I would need a way to keep track of heights that dont have spaces
        beteween them like the 7s and one 
        my brain is saying to use two pointers but i want to use a stack method to learn
        Use stack entries containing:

            the starting index where a height can begin
            the height

        As you scan from left to right:

            Set start to the current index.
            While the stack is nonempty and its top height is greater than the current height:
                Remove the top entry.
                Its rectangle ends immediately before the current index.
                Compute its width as current index - removed start index.
                Update the maximum area.
                Set start to the removed entry’s start index.
            Add the current height using start, not necessarily the current index.

        That last step is the key. If you pop bars that began earlier, the current shorter height can also begin at that earlier position.

        For [2, 1, 5, 6, 2, 3], when processing the second 2:

            6 ends at the previous index.
            5 also ends there and carries its earlier starting position backward.
            The new 2 uses that carried starting position, allowing it to span the 5, 6, and itself.
            It still cannot cross the earlier 1.
            '''
        n = len(heights)
        stack = []

        leftMost = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)

        stack = []
        rightMost = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)

        maxArea = 0
        for i in range(n):
            leftMost[i] += 1
            rightMost[i] -= 1
            maxArea = max(maxArea, heights[i] * (rightMost[i] - leftMost[i] + 1))
        return maxArea
