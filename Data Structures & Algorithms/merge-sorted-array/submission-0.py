class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        ''' 
        Input:
             Two integer arrays nums1 and nums2
             both sorted in non-decreasing order

             nums1 has a length of m+n where m is elements containing the values to be merge and n is elements set to 0 as placehodlers

             m - number of valid elements in nums 1
             n - number of elements in nums2
        Output:
             merge the two arrays into a sorted in non-decreasing order inside of nums1. 
        Goal: 
             modify nums1 in place and make sure to not return anything.
        

        Psedocode:
        we need a way to keep an index at the beginnig of both nums 1 and num2 where if the first index in nums 1 gets a zero which is the placeholder to replace the element at that index in nums 2 and after all the numbers are replaced sort that num1 array 
'''
        last = m + n - 1

        # Merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        #fill nums1 with leftover nums2 elements
        while n > 0: 
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1