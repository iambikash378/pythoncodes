#Given Two Strings word1 and word2
#Merge the strings by adding letters in alternating order, starting with word1
#If a string is longer than the other, append the additional letters onto the end of the merged string
#Return the merged string

def mergeAlternately(word1, word2):
    small_word, small_len = (word1, len(word1)) if len(word1) < len(word2) else (word2, len(word2))
    big_word, big_len = (word1 , len(word1)) if len(word1) > len(word2) else (word2, len(word2))
    appended_word = ''
    for index, (letter1, letter2) in enumerate(zip(word1, word2)):
            appended_word += letter1 + letter2
    appended_word += big_word[small_len : big_len]
    return appended_word


word1 = 'ab'
word2 ='pqrs'
word3 = mergeAlternately(word1,word2)
print(word3)