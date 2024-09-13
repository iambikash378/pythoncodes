class Solution:
    def search(self, nums: List[int], target: int) -> int:
        len_list = len(nums)
        left_index = 0
        right_index = len_list-1
        current_index = (left_index + right_index)//2
        while(left_index < right_index):
          if(nums[current_index] == target):
            return current_index
          elif (target < nums[current_index]):
            right_index = current_index-1
          else:
            left_index = current_index+1
        return left_index,right_index

