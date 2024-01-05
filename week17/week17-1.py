class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N=len(nums) #問題的長度
        ans=1
        table=[0]*N #放小答案的表格
        table[0]=1 #嘴簡單的問題的答案,就是我自己一個數字
        for i in range(1,N): #慢慢探索夠多的答案 table[i]
            table[i]=1 #最簡單的答案,還是我1個數字
            for k in range(i): #我要去查 table[0]...table[i-1]
                if nums[i]>nums[k] and table[k]+1>table[i]:
                    #我比你大,可以吃你,而且你的答案+我1個,會比我原本記下來的答案更好
                    table[i]=table[k]+1
            #經過上面的逐項檢查,確認table[i]就是問題num[i]的對應答案
            if table[i]>ans:ans=table[i] #更新後最大的答案
        return ans