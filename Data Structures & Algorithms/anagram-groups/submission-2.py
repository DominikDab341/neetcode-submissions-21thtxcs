class Solution:
    def isAnagram(self,a,b):
        a = list(a)
        a.sort()
        b = list(b)
        b.sort()
        if a == b: 
            return True
        else:
            return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}

        for i, word in enumerate(strs):
            potential_anagram = list(word)
            potential_anagram.sort()
            potential_anagram = "".join(potential_anagram)
            if potential_anagram in anagramDict:
                anagramDict[potential_anagram].append(word)
            else:
                anagramDict[potential_anagram] = []
                anagramDict[potential_anagram].append(word)
        return list(anagramDict.values())