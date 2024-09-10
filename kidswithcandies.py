class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current_greatest = max(candies)
        boolean_list = []
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= current_greatest :
              boolean_list.append(True)
            else:
              boolean_list.append(False)
        return boolean_list