from typing import List

class ArrayEasy:
    
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # nums = [2,7,11,15], target = 9
        res = dict()
        for index, num in enumerate(nums):
            diff = target - num
            if diff in res:
                return [res[diff],index]
            res[num] = index
        return []
    
    def merge_sorted_array(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

        last_index = m + n - 1

        while n > 0 and m > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last_index] = nums1[m-1]
                m -= 1
            else:
                nums1[last_index] = nums2[n-1]
                n -= 1
            last_index -= 1

        while n > 0:
            nums1[last_index] = nums2[n-1]
            last_index -= 1
            n -= 1

    def remove_elements(self, nums: List, val: int) -> int:
        # nums = [3,2,2,3], val = 3

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    
    def remove_duplicate_from_sorted_array(self, nums: List) -> int:
        # nums = [0,0,1,1,1,2,2,3,3,4]
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k

    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        res = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == res:
                count += 1
            else:
                count -= 1
                if count < 0:
                    count = 0
                    res = nums[i]

        return res
