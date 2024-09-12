class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedCharSet = set(allowed)
        count = 0
        isValid = True

        for word in words:
            for j in range(len(word)):
                if word[j] not in allowedCharSet:
                    isValid = False
                    break
            
            if isValid:
                count += 1
            isValid = True
        
        return count
            