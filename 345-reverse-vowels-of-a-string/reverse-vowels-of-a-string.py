class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=["a","A", "e","E", "i", "I", "o","O","u","U"]
        replace=[]
        for i in s:
            if i in vowels:
                replace.append(i)
        i=0
        j=0
        s=list(s)
        n=len(replace)
        while i<len(s) :
            if s[i] in vowels:
                s[i]=replace[n-1-j]
                j=j+1
            i=i+1

        return "".join(s)
