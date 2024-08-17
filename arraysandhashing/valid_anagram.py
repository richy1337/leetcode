class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}

        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        for char in t:
            if char not in char_count:
                return False
            elif char_count[char] == 0:
                return False
            else:
                char_count[char] -= 1


        values = char_count.values()
        for value in values:
            if value != 0:
                return False

        return True

'''
In this solution, we utilise a Hash Map to solve the problem in efficient time, taking advantage of the fact that getting a value in a Hash Map is O(1)

We first do a preliminary check if the two strings are of equal size. If not, return False because it is impossible for them to be anagrams if they are not the same size.

Initialise a Hash Map called char_count to store the frequency of characters in the first string.
Iterate through the characters in the first string and update char_count accordingly 

Then iterate through the characters in the second string and start 'checking off' the characters.

At the end, check if all the values in char_count are equal to 0.
If so, it means that they are anagrams, not anagrams otherwise.
'''
    

