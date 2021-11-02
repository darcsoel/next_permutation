from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) < 2:
            return None

        nums_count = len(nums)
        first_decrease_element_index = None

        for i in range(1, nums_count):
            prev_index = nums_count - i - 1
            cur_index = nums_count - i

            if nums[prev_index] < nums[cur_index]:
                first_decrease_element_index = prev_index
                break
        else:
            # if list is sorted desc - sorting in asc
            nums.sort()
            return None

        larger_than_first_decreased_index = None

        for i in range(first_decrease_element_index, nums_count):
            if nums[first_decrease_element_index] < nums[i]:
                if larger_than_first_decreased_index is None or nums[i] <= nums[larger_than_first_decreased_index]:
                    larger_than_first_decreased_index = i

        nums[first_decrease_element_index], nums[larger_than_first_decreased_index] = (
            nums[larger_than_first_decreased_index],
            nums[first_decrease_element_index],
        )

        to_rotate = first_decrease_element_index + 1
        nums[to_rotate:] = reversed(nums[to_rotate:])

        return None
