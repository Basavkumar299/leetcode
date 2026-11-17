class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1=len(word1)
        n2=len(word2)
        merge=[]
        i=0

        while i<n1 and i<n2:
            merge.append(word1[i])
            merge.append(word2[i])
            i=i+1
        if n1<n2:
            merge.append(word2[i:n2:1])
        else :
            merge.append(word1[i:n1])
        merge="".join(merge)
        return merge