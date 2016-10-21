class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        A = set(A.split(" "))
        print A
        if not B:
            return True
        B = set(B.split(" "))
        print B
        for b in B:
            if b not in A:
                return False
        return True

s = Solution()
s.compareStrings("sdaas", "das")

