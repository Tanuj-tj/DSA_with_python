from typing import List

class ArrayMedium:
    
    def remove_duplicate_from_sorted_array_ii(self, nums: List) -> int:
        # nums = [1,1,1,2,2,3]
        
        l = 0 
        r = 0

        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                count += 1
                r += 1

            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1

            r += 1

        return l


    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        def rotate_helper(start, end):
            while start < end:
                nums[start],nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # rotate the complete array
        rotate_helper(0,len(nums)-1)

        # Rotate the first kth elements
        rotate_helper(0, k-1)

        # Rotate the last kth elements
        rotate_helper(k, len(nums)-1)

    

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    val = 2
    array = ArrayMedium()
    print(array.remove_duplicate_from_sorted_array_ii(nums))
    print(nums)
