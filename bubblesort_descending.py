def bubblesort(list_of_num):
  list_len = len(list_of_num)
  while(list_len > 0):
    for i in range(list_len-1):
      if (list_of_num[i] < list_of_num[i+1]):
        list_of_num[i] , list_of_num[i+1] = list_of_num[i+1], list_of_num[i]
    list_len -= 1
  return list_of_num
    

list1 = [10,20,30,40,50]
print(bubblesort(list1)) 
