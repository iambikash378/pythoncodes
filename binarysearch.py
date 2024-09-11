def search( nums, target: int):
    len_list = len(nums)
    left_index = 0
    right_index = len_list-1
    while(left_index <= right_index):
      current_index = (left_index + right_index)//2
      if(nums[current_index] == target):
        return current_index
      elif (target < nums[current_index]):
        right_index = current_index-1
      else:
        left_index = current_index+1
      #print(left_index,right_index,current_index)
    return left_index,right_index

list = [1,3,10,45,60,100,101]
tar = 63
print(search(list, tar))