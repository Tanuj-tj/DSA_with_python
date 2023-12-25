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

    

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    val = 2
    array = ArrayMedium()
    print(array.remove_duplicate_from_sorted_array_ii(nums))
    print(nums)