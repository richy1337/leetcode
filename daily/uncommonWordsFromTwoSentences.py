class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        output = []
        wordsOne = s1.split(' ')
        wordsTwo = s2.split(' ')
        uncommonWords = defaultdict(int)
        for word in wordsOne:
            uncommonWords[word] += 1

        for word in wordsTwo:
            uncommonWords[word] += 1
        
        for key, value in uncommonWords.items():
            if value == 1:
                output.append(key)
            

        return output


        