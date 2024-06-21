class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common_prefix = ""
        index_min_no_of_letters = 0
        if strs == [""]:
            return longest_common_prefix
       

        min_no_of_letters = len(strs[0])
        for index, value in enumerate(strs):
            if len(value) < min_no_of_letters:
                min_no_of_letters = len(value)
                index_min_no_of_letters = index
        
        for i in range(min_no_of_letters):
            for word in strs:
                if (word[i] != strs[index_min_no_of_letters][i]) and (word != strs[index_min_no_of_letters]):
                    return longest_common_prefix
            longest_common_prefix += strs[index_min_no_of_letters][i]
        return longest_common_prefix
