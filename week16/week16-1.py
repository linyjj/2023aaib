class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        ans=0
        H={}
        for c in chars:
            if c in H:H[c]+=1
            else:H[c]=1

        for word in words:
            wordH={}
            for c in word:
                if c in wordH:wordH[c]+=1
                else:wordH[c]=1

            bad=0
            for c in wordH:
                if (c not in H)or wordH[c]>H[c]:
                    bad=1
            if bad==0:ans+=len(word)
        return ans