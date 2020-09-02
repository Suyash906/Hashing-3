class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequence_set = set()
        res_set = set()
        for i in range(len(s)-10+1):
            curr = s[i:i+10]
            if curr in sequence_set:
                res_set.add(curr)
            sequence_set.add(curr)
            
        return [curr for curr in res_set]
