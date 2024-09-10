def gcdOfStrings(str1, str2):
  small_length_string, large_length_string = (str1, str2) if len(str1)<len(str2) else (str2, str1)
 
  def find_factors(x):
    max_limit = int(x**(1/2))
    factors = []
    for i in range (1, max_limit+1):
      if x%i == 0 :
        if( i != x//i):          
          factors.extend([i, x//i])
        else:
          factors.append(i)
    return factors

  factors_of_small = find_factors(len(small_length_string))
  factors_of_large = find_factors(len(large_length_string))

  for i in range(1,len(large_length_string)+1):
    if len(str2)%i == 0:
      factors_of_large.append(i)
  
  for i in factors_of_small[::-1]:
    string_till_ith_index = small_length_string[:i]
    if (string_till_ith_index * (int(len(small_length_string)/i)) == small_length_string) and (string_till_ith_index * (int(len(large_length_string)/i)) == large_length_string):
      return string_till_ith_index
  
  return ''



str1 = 'bibibi'
str2 = 'bibi'

print(gcdOfStrings(str1, str2))