class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
        冒泡排序
        每次找到未排序list中最大的一个放到尾部
        Average: O(n^2)
        """
        def BubbleSort(nums):
            for j in range(len(nums)-1, 0, -1):
                for i in range(j):
                    if nums[i] > nums[i+1]:
                        nums[i], nums[i+1] = nums[i+1], nums[i]

            return nums

        """
        选择排序
        每次找到未排序中的最小的一个放到开头
        Average O(n^2)
        """
        def SelectionSort(nums):
            for i in range(len(nums)-1):
                index = i
                for j in range(i+1, len(nums)):
                    if nums[j] < nums[index]:
                        index = j
                nums[i], nums[index] = nums[index], nums[i]

            return nums

        """
        快速排序
        选定pivot, 按大小分成两个list, recursive
        Average: O(nlogn)
        """
        def QuickSort(nums):

            def partition(nums, l, r):
                if l > r:
                    return

                pivot = nums[l]
                i = l
                j = r
                while i != j:
                    while nums[j] >= pivot and i < j:
                        j -= 1
                    while nums[i] <= pivot and i < j:
                        i += 1
                    nums[i], nums[j] = nums[j], nums[i]

                nums[l], nums[i] = nums[i], nums[l]

                partition(nums, l, i-1)
                partition(nums, i+1, r)

                return nums

            def partition2(nums, l, r):

                if l > r:
                    return

                pivot_index = random.randint(l, r)
                pivot = nums[pivot_index]

                nums[pivot_index], nums[r] = nums[r], nums[pivot_index]

                index = l

                for i in range(l, r):
                    if nums[i] < pivot:
                        nums[i], nums[index] = nums[index], nums[i]
                        index += 1

                nums[index], nums[r] = nums[r], nums[index]


                partition(nums, l, index-1)
                partition(nums, index+1, r)

                return nums

            return partition(nums, 0, len(nums)-1)

        """
        插入排序
        每个待排序序列的第一个看成有序序列, 剩下的看成无序序列
        把每一个无序序列的元素插入到有序序列中。
        Average: O(n^2)
        """
        def InsertSort(nums):
            for i in range(len(nums)):
                tmp = nums[i]
                index = i-1
                while index >=0 and tmp < nums[index]:
                    nums[index+1] = nums[index]
                    index -= 1

                nums[index+1] = tmp

            return nums


        """
        归并排序
        自上而下递归，自下而上迭代
        Average: O(nlogn)
        """
        def merge(left, right):
            nums = []
            l = r = 0
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    nums.append(left[l])
                    l += 1
                elif left[l] >= right[r]:
                    nums.append(right[r])
                    r += 1
            return nums+left[l:]+right[r:]

        def MergeSort(nums):
            if len(nums) < 2:
                return nums
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]

            return merge(MergeSort(left), MergeSort(right))

        def MergeSortIterative(nums):
            interval = 1
            while interval < len(nums):
                for i in range(0, len(nums) - interval, 2*interval):
                    nums[i:i+2*interval] = merge(nums[i:i+interval], nums[i+interval:i+2*interval])
                interval *= 2

            return nums

        ans = MergeSortIterative(nums)

        return ans
