class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        #現在還沒寫完,先把week08-3的倆倆比較,寫出來
        N=len(arr) #小心,題目不是a是arr
        for k in range(N):
            for i in range(1,N):
                if arr[i]<arr[i-1]:
                    arr[i],arr[i-1]=arr[i-1],arr[i]

        for i in range(1,N):
            if arr[i]-arr[i-1]!=arr[1]-arr[0]:
                return False
        return True