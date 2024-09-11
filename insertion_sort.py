def insertion(list):
  listlen = len(list)
  for i in range(1,listlen):
    for j in range(i, 0, -1):
      if list[j] < list[j-1]:
        swap = list[j]
        list[j] = list[j-1]
        list[j-1] = swap
      else:
        break
  return list


list = [5,4,3,2,1]
print(insertion(list))