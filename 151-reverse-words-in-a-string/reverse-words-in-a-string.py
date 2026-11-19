class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        current = ""
        for char in s:
            if char != " ":
                current += char
            elif current:
                words.append(current)
                current = ""
        if current:
            words.append(current)
        words.reverse()
        return " ".join(words)
