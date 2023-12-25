from problems.array.easy import ArrayEasy

class Execute:

    @staticmethod
    def main():
        array = ArrayEasy()
        nums = [3,3]
        target = 6
        print(array.two_sum(nums, target))
        nums1 = [1,2,3,0,0,0] 
        m = 3
        nums2 = [2,5,6]
        n = 3
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        array.merge_sorted_array(nums1,m,nums2,n)
        print(nums1)



if __name__ == "__main__":
    Execute.main()