class Solution(object):
    def minMultuplication(self, sizes):
        n = len(sizes) - 1 # number of matrixes
        INT_MAX = 2 ** 31 - 1

        # T[i][j] = the minimum times of multiplication between Mi & Mj
        T = [[INT_MAX] * n for _ in xrange(n)]
        R = [[0] * n for _ in xrange(n) ]

        # optimal multiplication sequence
        seq = []

        # T[i][i + 1] = sizes[i - 1] * sizes[i] * sizes[i + 1]
        # only two matrix
        for i in xrange(1, n):
            T[i - 1][i] = sizes[i - 1] * sizes[i] * sizes[i + 1]
            R[i - 1][i] = i

        # T[i][i] = 0, only one matrix
        for i in xrange(n):
            T[i][i] = 0
            R[i][i] = i

        # T[i][j] = min(T[i][k] + T[k + 1][j] + sizes[i] * sizes[k] * sizes[j])
        # For i =< k < j
        # r: count range which is from 2 ~ (n - 1)
        # O(n^3)
        for r in xrange(2, n):
            for i in xrange(1, n - r + 1):
                j = i + r
                for k in xrange(i, j):
                    if(T[i - 1][k - 1] + T[k][j - 1] + sizes[i - 1] * sizes[k] * sizes[j] < T[i - 1][j - 1]):
                        T[i - 1][j - 1] = T[i - 1][k - 1] + T[k][j - 1] + sizes[i - 1] * sizes[k] * sizes[j]
                        R[i - 1][j - 1] = k
        
        for i in reversed(xrange(1, n)):
            seq.append(R[0][i])
        
        return T[0][n - 1]



sol = Solution()
sizes = [10, 100, 20, 15, 30, 50]
print sol.minMultuplication(sizes)

