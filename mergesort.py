
#Writing a code that merges two sorted arrays and sorts them

def merge_two_sorted_array(a, b):
  sorted_list = []
  len_a = len(a)
  len_b = len(b)
  i=j=0
  while (i < len_a) and (j < len_b):

    if (a[i] <= b[j]):
      #print(f"Comparing {a[i]} and {b[j]}, we find {a[i]} < {b[j]}. So, we increment i by 1")
      sorted_list.append(a[i])
      i+=1
    elif (a[i]>b[j]):
      #print(f"Comparing {a[i]} and {b[j]}, we find {b[j]} < {a[i]}. So, we increment j by 1")
      sorted_list.append(b[j])
      j+=1
    #print(f"i={i} and j = {j}. The sorted list is {sorted_list}")

  if i < len_a:
    sorted_list.extend(a[i:])

  if j < len_b:
    sorted_list.extend(b[j:])
     

  return sorted_list

def sort(list):

  if len(list) <= 1:
    return list #Returns sorted list
  
  else:
    mid = len(list) // 2
    left = list[:mid] 
    right = list[mid:]
    sorted_left = sort(left)
    sorted_right =sort(right)
    return merge_two_sorted_array(sorted_left,sorted_right)

a = [2,6,3,4,10,9,8]
print(sort(a))
#print(merge_two_sorted_array(b,c))