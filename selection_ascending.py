def selection_sort(list_num):
  list_len = len(list_num)
  iter = 0
  while(iter < list_len ):
    current_smallest = list_num[iter]
    smallest_index = iter
    for i in range(iter+1,list_len):
      if list_num[i] > current_smallest:
        #print(i,list_num[i], current_smallest)
        current_smallest = list_num[i]
        smallest_index = i
    #print("before exchaning", list_num)
    list_num[smallest_index], list_num[iter] = list_num[iter], list_num[smallest_index]
    iter+=1
    #print(iter-1,list_num)
  return list_num

list = [1,2,3,4,5]
print(selection_sort(list))
