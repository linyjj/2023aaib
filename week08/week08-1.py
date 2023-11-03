class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #1,3,9,27,81,243,...
        #程式還差1行!有個奇怪得問題會發生!沒檢查到0和-1
        if n<=0:
            return False
        while n>1: #到1為止
            if n%3 !=0: #沒辦法被3整除
                return False #失敗
            else:
                n=n//3

        #經過上面的while迴圈層層檢查,都沒失敗
        return True #那就是成功