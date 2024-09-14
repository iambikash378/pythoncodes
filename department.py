# 3 Departments i.e. fire, police and sanitation. They have to be assigned a unique number each from 1-7
# The sum of 3 numbers must be 12
# The number of police depatment must be even

def assign_num():
  police_possibilities = []
  combo = []

  for j in range(2,7,2):
    for k in range(1,8):
          l = 12-j-k
          if(j!=k and j!=l and k!=l and l <= 7 and l > 0):
            combo.append([j,k,l])
  print(combo)

assign_num()

 