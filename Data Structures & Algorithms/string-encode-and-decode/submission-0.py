class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded_string = ""
        for word in strs:
            # Używamy formatu: "5#Hello", "12#Niespodzianka"
            encoded_string += f"{len(word)}#{word}"
        return encoded_string

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            word_length = int(s[i:j])
            start = j + 1
            end = j + 1 + word_length
            result.append(s[start:end])
            i = end
            
        return result