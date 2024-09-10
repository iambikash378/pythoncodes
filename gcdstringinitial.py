def gcdOfStrings(str1, str2):
  small_length_string, large_length_string = (str1, str2) if len(str1)<len(str2) else (str2, str1)
  factors_of_small = []
  factors_of_large = []
  for i in range(1,len(small_length_string)+1):
    if len(str1) % i == 0:
      factors_of_small.append(i)

  for i in range(1,len(large_length_string)+1):
    if len(str2)%i == 0:
      factors_of_large.append(i)
  
  for i in factors_of_small[::-1]:
    string_till_ith_index = small_length_string[:i]
    if (string_till_ith_index * (int(len(small_length_string)/i)) == small_length_string) and (string_till_ith_index * (int(len(large_length_string)/i)) == large_length_string):
      return string_till_ith_index
  
  return ''



str1 = 'hellohello'
str2 = 'hello'

print(gcdOfStrings(str1, str2))
